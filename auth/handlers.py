"""Provides the endpoints for logging in and out.
Supports Google OAuth2.
"""

import tornado.auth
import tornado.gen

from common.common import BaseHandler
from settings import settings


class GoogleOAuth2LoginHandler(BaseHandler, tornado.auth.GoogleOAuth2Mixin):

    @tornado.gen.coroutine
    def get(self):
        if self.get_argument('code', False):
            user = yield self.get_authenticated_user(
                redirect_uri='%s/auth/google' % settings.SITE_URL,
                code=self.get_argument('code')
            )
            access_token = user['access_token']
            self.set_secure_cookie(settings.USER_COOKIE, access_token)

            self.redirect(self.get_argument("state", "/"))
            return
        else:
            yield self.authorize_redirect(
                redirect_uri='%s/auth/google' % settings.SITE_URL,
                client_id=settings.secure.google_oauth_key,
                scope=['email'],
                response_type='code',
                extra_params=dict(
                    approval_prompt='auto',
                    # TODO(Bieber): user login_hint,
                    state=self.get_argument("next", "/"),
                )
            )


class AuthLoginHandler(BaseHandler):
    # TODO(Bieber): Implement login screen
    def get(self):
        pass


class AuthLogoutHandler(BaseHandler):
    def get(self):
        self.clear_cookie(settings.USER_COOKIE)
        self.redirect(self.get_argument("next", "/"))


handlers = [
    (r"/auth/login", GoogleOAuth2LoginHandler),
    (r"/auth/google", GoogleOAuth2LoginHandler),
    (r"/auth/logout", AuthLogoutHandler),
]
