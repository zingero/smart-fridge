import logging

from ftpclient import FtpClient


class Main(object):
	def __init__(self):
		self._initLogging()
		self._ftpClient = FtpClient()
		self._ftpClient.uploadFile("/home/orian/Downloads/black.jpg")
		self._ftpClient.stop()

	def _initLogging(self):
		logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.DEBUG)


if __name__ == "__main__":
	Main()
