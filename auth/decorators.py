import tornado.web

def require_admin(func):

    @tornado.web.authenticated
    def inner(self, *args, **kwargs):
        user = self.get_current_user()
        email = user['email']
        if email not in ['david810@gmail.com', 'dbieber@princeton.edu']:
            self.redirect('/')
            return
        return func(self, *args, **kwargs)

    return inner
