from datetime import datetime
import redis
import tornado.web

from common.common import BaseHandler


MESSAGE_QUEUE = "sendlater:messages"

class SendLaterHandler(BaseHandler):
    def get(self):
        self.render("sendlater/index.html")

    def post(self):
        self.render("sendlater/index.html")

class SendLaterMessageHandler(BaseHandler):
    def initialize(self, redis_host="localhost", redis_port=6379):
        self.redis = redis.StrictRedis(host=redis_host, port=redis_port, db=0)

    def get(self):
        all_messages = self.redis.lrange(MESSAGE_QUEUE, 0, -1)
        for message in all_messages:
            self.write(message)
            self.write('<br/>\n')

    def post(self):

        message = self.get_argument("message")
        recipient = self.get_argument("recipient")
        sender = self.get_argument("sender")

        # Two methods of setting "when". Try them both.
        try:
            when = self.get_argument("when")
        except:
            when_1 = self.get_argument("when_1")  # hour
            when_2 = self.get_argument("when_2")  # minute
            when_3 = self.get_argument("when_3")  # second
            when_4 = self.get_argument("when_4")  # AM/PM
            when = "{}:{} {}".format(when_1, when_2, when_4)

        modified = datetime.now()

        self.redis.rpush(MESSAGE_QUEUE, {
            'message': message,
            'sender': sender,
            'recipient': recipient,
            'when': when,
            'modified': modified
        })

handlers = [
    (r'/sendlater/message/?', SendLaterMessageHandler),
    (r'/sendlater/?', SendLaterHandler),
]
