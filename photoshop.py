import os
from PIL import Image

import tongue


def is_photo_dark(file_path):
	assert os.path.exists(file_path)
	pixels = Image.open(file_path).convert('L').getdata()

	dark_pixels_number = 0
	for pixel in pixels:
		if pixel < tongue.DARK_PIXEL_THRESHOLD:
			dark_pixels_number += 1
	return (dark_pixels_number / float(len(pixels))) > tongue.DARK_PICTURE_THRESHOLD
