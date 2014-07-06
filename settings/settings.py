try:
    import secure_settings as secure
except:
    import secure_settings_template as secure

SITE_URL = 'http://localhost:8000' or 'http://www.davidbieber.com'
USER_COOKIE = 'user'
