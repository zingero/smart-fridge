import os
from PIL import Image

import configuration


def is_photo_clear(file_path):
	assert os.path.exists(file_path)
	pixels = Image.open(file_path).convert('L').getdata()
	return not (is_photo_dark(pixels) or is_photo_bright(pixels))


def is_photo_dark(pixels):
	dark_pixels_number = 0
	for pixel in pixels:
		if pixel < configuration.DARK_PIXEL_THRESHOLD:
			dark_pixels_number += 1
	return (dark_pixels_number / float(len(pixels))) > configuration.DARK_PICTURE_THRESHOLD


def is_photo_bright(pixels):
	bright_pixels_number = 0
	for pixel in pixels:
		if pixel > configuration.BRIGHT_PIXEL_THRESHOLD:
			bright_pixels_number += 1
	return (bright_pixels_number / float(len(pixels))) > configuration.BRIGHT_PICTURE_THRESHOLD


def rotate_photo(file_path):
	if configuration.ROTATION_ANGLE != 0:
		image = Image.open(file_path)
		image = image.rotate(angle = configuration.ROTATION_ANGLE, expand = True)
		image.save(file_path)
