import json

import tongue

configuration = dict(
	REMOTE_CAPTURES_FOLDER = 'smartfridge',
	MAXIMUM_FILES_IN_REMOTE_FOLDER = 100,

	DARK_PIXEL_THRESHOLD = 50,			# 0-255
	DARK_PICTURE_THRESHOLD = 0.5,		# 0-1
	BRIGHT_PIXEL_THRESHOLD = 200,		# 0-255
	BRIGHT_PICTURE_THRESHOLD = 0.5,		# 0-1
	ROTATION_ANGLE = 0					# In degrees
)

with open(tongue.CONFIGURATION_FILE_PATH) as configuration_file:
	configuration.update(json.loads(configuration_file.read()))

globals().update(configuration)
