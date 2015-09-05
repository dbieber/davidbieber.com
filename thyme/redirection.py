import tornado.web

class RedirectHandler(tornado.web.RequestHandler):

    def prepare(self):

        if self.request.protocol == 'http':
            self.redirect(
                'https://%s' % self.request.full_url()[len('http://'):],
                permanent=True,
            )


handlers = [
    (r'/.*', RedirectHandler),
]

redirection_application = tornado.web.Application(
    handlers,
)
