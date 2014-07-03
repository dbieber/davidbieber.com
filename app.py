import os

import tornado.ioloop
import tornado.web

handlers = [
#    (r'/', tornado.web.StaticFileHandler, {'path': 'static', 'default_filename': 'index.html'}),
    (r'/(.*)', tornado.web.StaticFileHandler, {'path': 'static', 'default_filename': 'index.html'}),
]

settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
}

application = tornado.web.Application(handlers, **settings)

if __name__ == "__main__":
    port = 80
    application.listen(port)
    tornado.ioloop.IOLoop.instance().start()
