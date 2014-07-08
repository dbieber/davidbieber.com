from __future__ import absolute_import

try:
    import settings.secure_settings as secure
except:
    import settings.secure_settings_template as secure

SITE_URL = 'http://localhost:8000' or 'http://www.davidbieber.com'
USER_COOKIE = 'user'
