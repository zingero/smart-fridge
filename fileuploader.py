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
		self.__thread = Thread(target = self.run, name = "File Uploader")
		self.__thread.start()

	def upload_file(self, file_path):
		self.__queue.put(file_path)
		logging.info(f"File: {file_path} added to queue. Pending files quantity: {self.__queue.qsize()}")

	def run(self):
		while not self.__stopped:
			file_path = self.__queue.get()
			if file_path == tongue.POISON_PILL:
				break
			self.__client.upload_file(file_path)

	def stop(self):
		logging.info("Stopping file uploader")
		self.__stopped = True
		self.__queue.put(tongue.POISON_PILL)
		self.__thread.join()
		self.__client.stop()
