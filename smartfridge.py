import logging
import os

import photoshop
from camera import Camera
from fileuploader import FileUploader


class SmartFridge:
	def __init__(self, should_stop_function):
		self.__should_stop_function = should_stop_function
		self.__fileUploader = FileUploader()
		self.__camera = Camera()

	def start(self):
		while not self.__should_stop_function():
			try:
				self.__runningIteration()
			except Exception as e:
				logging.exception(f"Running failure: {e}")
				return

	def __runningIteration(self):
		file_path = self.__camera.capture()
		if file_path:
			if photoshop.is_photo_dark(file_path):
				os.remove(file_path)
			else:
				self.__fileUploader.upload_file(file_path)

	def stop(self):
		self.__fileUploader.stop()