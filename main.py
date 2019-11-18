import logging
import os
import threading
import datetime
import cv2
import signal

import photoshop
import tongue
from fileuploader import FileUploader


class Main(object):
	def __init__(self):
		signal.signal(signal.SIGTERM, self.__stop)
		signal.signal(signal.SIGINT, self.__stop)
		self.__event = threading.Event()
		self.__initLogging()
		self.__fileUploader = FileUploader()
		self.__run()
		self.__fileUploader.stop()
		logging.info("Process terminated")

	def __initLogging(self):
		logging.basicConfig(format = '%(asctime)s %(levelname)s %(message)s', level = logging.DEBUG)
		logging.getLogger('googleapiclient.discovery_cache').setLevel(logging.ERROR)

	def __getImage(self, camera):
		_, image = camera.read()
		return image

	def __run(self):
		while not self.__event.isSet():
			logging.info("in run")
			camera_port = 0
			# camera = cv2.VideoCapture()
			camera = cv2.VideoCapture(camera_port)

			capture = self.__getImage(camera)
			filePath = os.path.join(tongue.CAPTURES_FOLDER, datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S") + ".png")
			cv2.imwrite(filePath, capture)
			# if photoshop.isPhotoDark(filePath):
			# 	self.__fileUploader.uploadFile(filePath)
			self.__event.wait(timeout = 1)
			# self.__event.wait(timeout = 0.1)

	def __stop(self, signalNumber, frame):
		signal.signal(signalNumber, signal.SIG_IGN)
		self.__event.set()


if __name__ == "__main__":
	Main()
