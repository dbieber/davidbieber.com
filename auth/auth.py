from __future__ import absolute_import

import json
import tornado.auth
import tornado.gen
import tornado.web

try:
    from urllib.request import urlopen
except:
    from urllib2 import urlopen

from settings import settings


"""Every RequestHandler should extend this in order to access the current user
"""
class BaseHandler(tornado.web.RequestHandler):

    def get_current_user(self):
        """Determines if the user is logged in.
        Returns the current user object if the user is logged in.
        Returns None if the user is not logged in.
        """
        access_token = self.get_secure_cookie(settings.USER_COOKIE)
        if not access_token:
            return None
        access_token = access_token.decode("utf-8")

        # Fetch email. TODO(Bieber): Cache it, stick it in a database, don't do this every time.
        url_pattern = ('https://www.googleapis.com/plus/v1/people/{user_id}' \
                       '?access_token={access_token!s}' \
                       '&fields=emails')
        url = url_pattern.format(
            user_id='me',
            access_token=str(access_token),
            key=settings.secure.google_oauth_key,
        )

        try:
            response = urlopen(url)
            out = response.read().decode("utf-8")
            data = json.loads(out)

            email_struct = data['emails'][0]
            email = email_struct['value']
        except:
            self.clear_cookie(settings.USER_COOKIE)
            email = None

        user = dict(
            access_token=access_token,
            email=email
        )

        return user


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


class AuthLogoutHandler(BaseHandler):
    def get(self):
        self.clear_cookie(settings.USER_COOKIE)
        self.redirect(self.get_argument("next", "/"))


handlers = [
    (r"/auth/google", GoogleOAuth2LoginHandler),
    (r"/auth/logout", AuthLogoutHandler),
]
