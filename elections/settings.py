from django.conf import settings

DEFAULT_SETTINGS = {
    'TEST_DATA_ONLY': False,
    'FTP_USER': 'anonymous',
    'FTP_PASSWORD': '',
    'FTP_HOST': '',
    'DOWNLOAD_PATHS': [],
    'DEST_PATH': '/tmp/election/',
    'IMAGE_MODEL': None,
    'IMAGE_STORAGE': settings.DEFAULT_FILE_STORAGE,
}

USER_SETTINGS = DEFAULT_SETTINGS.copy()
USER_SETTINGS.update(getattr(settings, 'ELECTIONS_SETTINGS', {}))

globals().update(USER_SETTINGS)