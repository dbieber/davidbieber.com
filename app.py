import argparse
import os
import sys

import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.auth

from settings import settings

from auth.handlers import handlers as auth_handlers
from sendlater.sendlater import handlers as sendlater_handlers
from thyme.thyme import handlers as thyme_handlers
from thyme.redirection import redirection_application


def main():
    parser = argparse.ArgumentParser(description='Launch davidbieber.com')
    parser.add_argument('--ssl', default=True, action='store_true',
                        help='Require ssl')
    parser.add_argument('--no-ssl', dest='ssl', action='store_false',
                        help='Do not require ssl')
    parser.add_argument('--redirect', default=False, action='store_true',
                        help='Redirect http to https')
    parser.add_argument('--certfile', type=str, default=settings.secure.certfile,
                        help='Path to SSL certfile')
    parser.add_argument('--keyfile', type=str, default=settings.secure.keyfile,
                        help='Path to SSL keyfile')
    parser.add_argument('--port', type=int, default=8000, help='Port for davidbieber.com')

    args = parser.parse_args()
    ssl = args.ssl
    certfile = args.certfile
    keyfile = args.keyfile
    port = args.port
    redirect = args.redirect

    handlers = (
        auth_handlers +
        sendlater_handlers +
        thyme_handlers +
        [
            # Since static and default are relative paths, app.py must be run from this directory.
            (r'/static/(.*)', tornado.web.StaticFileHandler, {'path': 'static', 'default_filename': 'index.html'}),
            (r'/(.*)', tornado.web.StaticFileHandler, {'path': 'default', 'default_filename': 'index.html'}),
        ]
    )

    tornado_settings = dict(
        debug=settings.secure.debug,
        xsrf_cookies=False,
        cookie_secret=settings.secure.cookie_secret,
        login_url='/auth/google',
        google_oauth=dict(
            key=settings.secure.google_oauth_key,
            secret=settings.secure.google_oauth_secret,
        )
    )

    application = tornado.web.Application(
        handlers,
        **tornado_settings
    )

    if ssl:
        assert certfile is not None
        assert keyfile is not None
        server = tornado.httpserver.HTTPServer(application, ssl_options={
            'certfile': certfile,
            'keyfile': keyfile,
        })
        assert port == 443
        server.listen(port)
        if redirect:
            redirection_application.listen(80)
    else:
        application.listen(port)

    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
