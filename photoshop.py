import os
from PIL import Image

import tongue


def isPhotoDark(filePath):
	assert os.path.exists(filePath)
	pixels = Image.open(filePath).convert('L').getdata()

	darkPixelsNumber = 0
	for pixel in pixels:
		if pixel < tongue.DARK_PIXEL_THRESHOLD:
			darkPixelsNumber += 1
	return (darkPixelsNumber / float(len(pixels))) > tongue.DARK_PICTURE_THRESHOLD
