import logging

from fileuploader import FileUploader


class Main(object):
	def __init__(self):
		self._initLogging()
		self.__fileUploader = FileUploader()
		self.__fileUploader.uploadFile("/home/orian/Downloads/cat.jpg")
		self.__fileUploader.stop()

	def _initLogging(self):
		logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.DEBUG)


if __name__ == "__main__":
	Main()
