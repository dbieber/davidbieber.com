from __future__ import absolute_import

import json
import tornado.web

try:
    from urllib.request import urlopen
except:
    from urllib2 import urlopen

from settings import settings


"""Every RequestHandler should extend this in order to access the current user
"""
class AuthEnabledRequestHandler(tornado.web.RequestHandler):

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
            return None

        user = dict(
            access_token=access_token,
            email=email
        )

        return user
