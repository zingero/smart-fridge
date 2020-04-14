import os
from PIL import Image

import tongue


def is_photo_clear(file_path):
	assert os.path.exists(file_path)
	pixels = Image.open(file_path).convert('L').getdata()
	return not (is_photo_dark(pixels) or is_photo_bright(pixels))


def is_photo_dark(pixels):
	dark_pixels_number = 0
	for pixel in pixels:
		if pixel < tongue.DARK_PIXEL_THRESHOLD:
			dark_pixels_number += 1
	return (dark_pixels_number / float(len(pixels))) > tongue.DARK_PICTURE_THRESHOLD


def is_photo_bright(pixels):
	bright_pixels_number = 0
	for pixel in pixels:
		if pixel > tongue.BRIGHT_PIXEL_THRESHOLD:
			bright_pixels_number += 1
	return (bright_pixels_number / float(len(pixels))) > tongue.BRIGHT_PICTURE_THRESHOLD
