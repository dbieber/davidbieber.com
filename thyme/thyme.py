from auth.auth import BaseHandler

import tornado.web
import tornado.auth

from datetime import datetime
from datetime import timedelta

from transactions import TransactionLoader
from transactions import TransactionAccumulator


class ThymeHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self):
        # TODO(Bieber): Move this into a decorator @require_admin
        user = self.get_current_user()
        email = user['email']
        if (email != "david810@gmail.com" and email != "dbieber@princeton.edu"):
            self.redirect('/')
            return

        loader = TransactionLoader(use_dropbox=True)
        accumulator = TransactionAccumulator(drop_change=False)

        threshold_datetime = datetime.now() - timedelta(days=999)

        self.write("<pre>")
        for transaction in loader.transactions:
            if transaction.get_datetime() >= threshold_datetime:
                accumulator.handle_transaction(transaction)
                delta = transaction.get_net_delta()
                balance = accumulator.get_delta()
                self.write("%-40s %.2f (%.2f) <br/>" % (transaction, balance, delta))

        self.write("Balance: %.2f<br/>" % accumulator.get_balance())
        self.write("Delta: %.2f<br/>" % accumulator.get_delta())
        elapsed_time = accumulator.last_datetime - accumulator.first_datetime
        elapsed_days = (elapsed_time.total_seconds() / timedelta(days=1).total_seconds())

        self.write("Days: %.2f<br/>" % elapsed_days)
        self.write("Rate: %.2f per day<br/>" % (accumulator.get_delta() / elapsed_days))
        self.write("In pocket: %.2f<br/>" % accumulator.get_balance('cash'))
        self.write("</pre>")



handlers = [
    (r'/thyme/', ThymeHandler),
]
