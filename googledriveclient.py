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

	def uploadFile(self, filePath):
		logging.info(f"Uploading file: {filePath}")
		metadata = {'name': os.path.basename(filePath)}
		try:
			media = MediaFileUpload(filePath)
			self.__service.files().create(body = metadata, media_body = media, fields = 'id').execute()
			logging.info(f"File: {filePath} uploaded successfully")
		except OSError as e:
			logging.warning(f"Failed to open file: {filePath}. Exception: {e}")
		except Exception as e:
			logging.exception(f"General Error: Failed to upload file: {filePath}. Exception: {e}")

	def listFiles(self, howMany):
		results = self.__service.files().list(pageSize=howMany, fields="nextPageToken, files(id, name)").execute()
		logging.info(f"Files list: {results.get('files', [])}")
