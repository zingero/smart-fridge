import logging
import ftplib
import os

import tongue
import credentials

from abstractclient import AbstractClient


class FtpClient(AbstractClient):
	def _login(self):
		self._ftpClient = ftplib.FTP(tongue.FTP_SERVER_ON_000WEBHOST_URL)
		self._ftpClient.login(credentials.username, credentials.password)
		logging.info("FTP client was connected successfully")

	def upload_file(self, file_path):
		logging.info(f"Uploading file: {file_path}")
		try:
			with open(file_path, "rb") as f:
				self._ftpClient.storbinary("STOR " + os.path.join("/photos", os.path.basename(file_path)), f)
			logging.info(f"File: {file_path} uploaded successfully")
		except OSError as e:
			logging.warning(f"Failed to open file: {file_path}. Exception: {e}")
		except ftplib.all_errors as e:
			logging.error(f"FTP Error: Failed to upload file: {file_path}. Exception: {e}")
		except Exception as e:
			logging.exception(f"General Error: Failed to upload file: {file_path}. Exception: {e}")

	def stop(self):
		logging.info("Stopping FTP client")
		self._ftpClient.quit()
