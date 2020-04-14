# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive']
GOOGLE_DRIVE_CREDENTIALS_FILE_PATH = '/etc/smartfridge/credentials.json'
GOOGLE_DRIVE_TOKEN_FILE_PATH = '/etc/smartfridge/token.pickle'
LOCAL_CAPTURES_FOLDER = '/var/smartfridge/'
REMOTE_CAPTURES_FOLDER = 'smartfridge'
FOLDER_MIME_TYPE = 'application/vnd.google-apps.folder'
PNG_MIME_TYPE = 'image/png'
MAXIMUM_FILES_IN_REMOTE_FOLDER = 100

DARK_PIXEL_THRESHOLD = 50  # 0-255
DARK_PICTURE_THRESHOLD = 0.5  # 0-1

POISON_PILL = "POISON PILL"
