import os
import sys

import tornado.ioloop
import tornado.web
import tornado.auth

from settings import settings

from auth.handlers import handlers as auth_handlers
from sendlater.sendlater import handlers as sendlater_handlers
from thyme.thyme import handlers as thyme_handlers


handlers = (
    auth_handlers +
    sendlater_handlers +
    thyme_handlers +
    [
        (r'/static/(.*)', tornado.web.StaticFileHandler, {'path': 'static', 'default_filename': 'index.html'}),
        (r'/(.*)', tornado.web.StaticFileHandler, {'path': 'default', 'default_filename': 'index.html'}),
    ]
)

tornado_settings = dict(
    xsrf_cookies=True,
    cookie_secret=settings.secure.cookie_secret,
    login_url='/auth/google',
    google_oauth=dict(
        key=settings.secure.google_oauth_key,
        secret=settings.secure.google_oauth_secret,
    )
)

application = tornado.web.Application(handlers, **tornado_settings)

def main():
    try:
        port = int(sys.argv[1])
    except:
        # TODO(Bieber): Use local settings
        port = 8000

    application.listen(port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
