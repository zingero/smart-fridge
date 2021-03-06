import os
import logging
from queue import Queue
from threading import Thread

import tongue
from googledriveclient import GoogleDriveClient


class FileUploader:
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
			os.remove(file_path)

	def stop(self):
		logging.info("Stopping file uploader")
		self.__stopped = True
		self.__queue.put(tongue.POISON_PILL)
		self.__thread.join()
		self.__client.stop()
		self.__remove_all_local_captures()

	def __remove_all_local_captures(self):
		captures = os.listdir(tongue.LOCAL_CAPTURES_FOLDER)
		logging.warning(f"Removing: {len(captures)} photos before uploading them")
		for capture in captures:
			os.remove(os.path.join(tongue.LOCAL_CAPTURES_FOLDER, capture))
