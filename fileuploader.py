import logging
from queue import Queue
from threading import Thread

import tongue
from googledriveclient import GoogleDriveClient


class FileUploader(object):
	def __init__(self):
		self.__stopped = False
		self.__queue = Queue()
		self.__client = GoogleDriveClient()
		self.__thread = Thread(target=self.run, name="File Uploader")
		self.__thread.start()

	def uploadFile(self, filePath):
		self.__queue.put(filePath)
		logging.info("File: %s added to queue" % filePath)

	def run(self):
		while True:
			filePath = self.__queue.get()
			if filePath == tongue.POISON_PILL:
				break
			self.__client.uploadFile(filePath)

	def stop(self):
		logging.info("Stopping file uploader")
		self.__stopped = True
		self.__queue.put(tongue.POISON_PILL)
		self.__thread.join()
		self.__client.stop()
