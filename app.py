import os
import sys

import tornado.ioloop
import tornado.web

handlers = [
    (r'/(.*)', tornado.web.StaticFileHandler, {'path': 'static', 'default_filename': 'index.html'}),
]

settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
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
