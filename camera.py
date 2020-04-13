import logging
import os
import datetime
import cv2

import tongue


class Camera(object):
	def __init__(self):
		self.__camera = cv2.VideoCapture(0)

	def capture(self):
		try:
			successfully_captured, image = self.__camera.read()
			if not successfully_captured:
				return
			file_path = os.path.join(tongue.LOCAL_CAPTURES_FOLDER,
									datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S") + ".png")
			cv2.imwrite(file_path, image)
			return file_path
		except cv2.error as e:
			logging.debug(f"Failed to capture an image. Did you connect a camera?. Exception: {e}")


if __name__ == "__main__":
	camera = Camera()
	print(f"Image is located at: {camera.capture()}")
