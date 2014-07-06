import os
import sys

import tornado.ioloop
import tornado.web

from sendlater import sendlater

handlers = sendlater.handlers + [
    (r'/(.*)', tornado.web.StaticFileHandler, {'path': 'static', 'default_filename': 'index.html'}),
]

settings = {
}

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
