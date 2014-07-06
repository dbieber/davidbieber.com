import os
import sys

import tornado.ioloop
import tornado.web
import tornado.auth

from sendlater import sendlater
from thyme import thyme
import auth

try:
    import secure_settings as settings
except:
    import secure_settings_template as settings


handlers = (
    sendlater.handlers +
    thyme.handlers +
    auth.handlers +
    [
        (r'/(.*)', tornado.web.StaticFileHandler, {'path': 'static', 'default_filename': 'index.html'}),
    ]
)

settings = dict(
    xsrf_cookies=True,
    cookie_secret=settings.cookie_secret,
    login_url='/auth/login',
)

application = tornado.web.Application(handlers, **settings)

def main():
    try:
        port = int(sys.argv[1])
    except:
        port = 8000

    application.listen(port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
