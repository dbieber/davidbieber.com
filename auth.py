from common import BaseHandler, USER_COOKIE

import tornado.auth
import tornado.web



class AuthLoginHandler(BaseHandler, tornado.auth.GoogleMixin):
    @tornado.web.asynchronous
    def get(self):
        if self.get_argument('openid.mode', None):
            self.get_authenticated_user(self.async_callback(self._on_auth))
            return
        self.authenticate_redirect()

    def _on_auth(self, user):
        if not user:
            raise tornado.web.HTTPError(500, 'Google auth failed')
        email = user['email']
        # TODO(Bieber): Update database with user information
        self.set_secure_cookie(USER_COOKIE, email)
        self.redirect(self.get_argument("next", "/"))


class AuthLogoutHandler(BaseHandler):
    def get(self):
        self.clear_cookie(USER_COOKIE)
        self.redirect(self.get_argument("next", "/"))


handlers = [
    (r"/auth/login", AuthLoginHandler),
    (r"/auth/logout", AuthLogoutHandler),
]
