import tornado.web


USER_COOKIE = 'user'

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        """Determines if the user is logged in.
        Returns the current user object if the user is logged in.
        Returns None if the user is not logged in.
        """
        user_id = self.get_secure_cookie(USER_COOKIE)
        if not user_id:
            return None
        return user_id
