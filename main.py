import logging
import ftplib
import os

import tongue


class Main(object):
	def __init__(self):
		self._initLogging()
		self._initCredentials()
		self._initFtpClient()

	def _initLogging(self):
		logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.DEBUG)

	def _initCredentials(self):
		if os.path.exists(tongue.CREDENTIALS_FILE_PATH):
			import credentials
			self._username = credentials.username
			self._password = credentials.password
		else:
			with open(tongue.CREDENTIALS_FILE_PATH, "w") as credentialsFile:
				credentialsFile.write('username = ""\npassword = ""\n')
				logging.warning("Enter your credentials in: %s" % tongue.CREDENTIALS_FILE_PATH)

	def _initFtpClient(self):
		self._ftpClient = ftplib.FTP(tongue.FTP_SERVER_URL)
		self._ftpClient.login(self._username, self._password)
		logging.info("FTP client was connected successfully. Welcome message: %s" % self._ftpClient.welcome())


if __name__ == "__main__":
	Main()
