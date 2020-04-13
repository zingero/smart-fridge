import logging
import threading
import signal

import photoshop
from camera import Camera
from fileuploader import FileUploader


class Main(object):
	def __init__(self):
		signal.signal(signal.SIGTERM, self.__stop)
		signal.signal(signal.SIGINT, self.__stop)
		self.__event = threading.Event()
		self.__initLogging()
		self.__fileUploader = FileUploader()
		self.__camera = Camera()
		self.__run()
		self.__fileUploader.stop()
		logging.info("Process terminated")

	def __initLogging(self):
		logging.basicConfig(format = '%(asctime)s %(levelname)s %(message)s', level = logging.INFO)
		logging.getLogger('googleapiclient.discovery_cache').setLevel(logging.ERROR)

	def __run(self):
		while not self.__event.isSet():
			self.__runningIteration()
			self.__event.wait(timeout = 1)
			# self.__event.wait(timeout = 0.1)

	def __runningIteration(self):
		file_path = self.__camera.capture()
		if file_path and not photoshop.is_photo_dark(file_path):
			self.__fileUploader.upload_file(file_path)

	def __stop(self, signalNumber, frame):
		signal.signal(signalNumber, signal.SIG_IGN)
		self.__event.set()


if __name__ == "__main__":
	Main()
