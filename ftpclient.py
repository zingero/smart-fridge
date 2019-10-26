import logging
import ftplib
import os

import tongue
import credentials


class FtpClient(object):
	def __init__(self):
		self._ftpClient = ftplib.FTP(tongue.FTP_SERVER_URL)
		self._ftpClient.login(credentials.username, credentials.password)
		logging.info("FTP client was connected successfully. Welcome message: %s" % self._ftpClient.welcome)

	def uploadFile(self, filePath):
		logging.info("Uploading file: %s" % filePath)
		try:
			with open(filePath, "rb") as f:
				self._ftpClient.storbinary("STOR " + os.path.join("/photos", os.path.basename(filePath)), f)
			logging.info("File: %s uploaded successfully" % filePath)
		except OSError as e:
			logging.warning("Failed to open file: %s. Exception: %s" % (filePath, e))
		except ftplib.all_errors as e:
			logging.error("Failed to upload file: %s. Exception: %s" % (filePath, e))

	def stop(self):
		self._ftpClient.quit()
