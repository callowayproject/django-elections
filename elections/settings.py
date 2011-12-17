from django.conf import settings

DEFAULT_SETTINGS = {
    'TEST_DATA_ONLY': False
}

USER_SETTINGS = DEFAULT_SETTINGS.copy()
USER_SETTINGS.update(getattr(settings, 'ELECTIONS_SETTINGS', {}))

first_level = ['AK', 'MD']
second_level = ['dbready']



globals().update(USER_SETTINGS)