from __future__ import print_function
import logging
import os
import pickle

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaFileUpload

import tongue
from abstractclient import AbstractClient


class GoogleDriveClient(AbstractClient):
	def __init__(self):
		super().__init__()
		if self.__is_remote_folder_exists():
			logging.info("Remote folder exists. Not creating")
		else:
			logging.info("Remote folder does not exists. Creating")
			self.__create_remote_folder()

	def _login(self):
		credentials = None
		if os.path.exists(tongue.GOOGLE_DRIVE_TOKEN_FILE_PATH):
			with open(tongue.GOOGLE_DRIVE_TOKEN_FILE_PATH, 'rb') as token:
				credentials = pickle.load(token)
		if not credentials or not credentials.valid:
			if credentials and credentials.expired and credentials.refresh_token:
				credentials.refresh(Request())
			else:
				flow = InstalledAppFlow.from_client_secrets_file(tongue.GOOGLE_DRIVE_CREDENTIALS_FILE_PATH, tongue.SCOPES)
				credentials = flow.run_local_server(port = 0)
		with open(tongue.GOOGLE_DRIVE_TOKEN_FILE_PATH, 'wb') as token:
			pickle.dump(credentials, token)
		self.__service = build('drive', 'v3', credentials = credentials)
		logging.info("Google drive client was connected successfully")

	def __is_remote_folder_exists(self):
		files = self.__search_for_remote_folder_id()
		if files:
			self.__folder_id = files[0]['id']
			return True
		return False

	def __search_for_remote_folder_id(self):
		results = self.__service.files().list(q = f"name='{tongue.REMOTE_CAPTURES_FOLDER}'", fields = "nextPageToken, files(id)").execute()
		files = results.get('files', [])
		assert len(files) <= 1, f"There are more than one '{tongue.REMOTE_CAPTURES_FOLDER}' folder in google drive. Results: {results}"
		return files

	def __create_remote_folder(self):
		metadata = {
			'name': tongue.REMOTE_CAPTURES_FOLDER,
			'mimeType': tongue.FOLDER_MIME_TYPE
		}
		file = self.__service.files().create(body = metadata, fields = 'id').execute()
		self.__folder_id = file.get('id')

	def upload_file(self, file_path):
		logging.info(f"Uploading file: {file_path}")
		metadata = {'name': os.path.basename(file_path), 'parents': [self.__folder_id]}
		try:
			media = MediaFileUpload(file_path)
			self.__service.files().create(body = metadata, media_body = media, fields = 'id').execute()
			logging.info(f"File: {file_path} uploaded successfully")
		except OSError as e:
			logging.warning(f"Failed to open file: {file_path}. Exception: {e}")
		except Exception as e:
			logging.exception(f"General Error: Failed to upload file: {file_path}. Exception: {e}")
