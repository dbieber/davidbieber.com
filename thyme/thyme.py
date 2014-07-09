from __future__ import absolute_import

import tornado.web
import tornado.auth

from collections import defaultdict
from datetime import datetime
from datetime import timedelta

from common.common import BaseHandler
from common.common import TemplateHandler
from thyme.transactions import TransactionLoader
from thyme.transactions import TransactionAccumulator


class ThymeHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self):
        # TODO(Bieber): Move this into a decorator @require_admin
        user = self.get_current_user()
        email = user['email']
        if (email != 'david810@gmail.com' and email != 'dbieber@princeton.edu'):
            self.redirect('/')
            return

        loader = TransactionLoader(use_dropbox=True)
        accumulator = TransactionAccumulator(drop_change=True)

        threshold_datetime = datetime.now() - timedelta(days=999)

        self.write('<pre>')
        for transaction in loader.transactions:
            if transaction.get_datetime() >= threshold_datetime:
                accumulator.handle_transaction(transaction)
                delta = transaction.get_net_delta()
                balance = accumulator.get_delta()
                self.write('%-40s %.2f (%.2f) <br/>' % (transaction, balance, delta))

        self.write('Balance: %.2f<br/>' % accumulator.get_balance())
        self.write('Delta: %.2f<br/>' % accumulator.get_delta())
        elapsed_time = accumulator.last_datetime - accumulator.first_datetime
        elapsed_days = (elapsed_time.total_seconds() / timedelta(days=1).total_seconds())

        self.write('Days: %.2f<br/>' % elapsed_days)
        self.write('Rate: %.2f per day<br/>' % (accumulator.get_delta() / elapsed_days))
        self.write('In pocket: %.2f<br/>' % accumulator.get_balance('cash'))
        self.write('</pre>')


class ThymeByDayHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self):
        # TODO(Bieber): Move this into a decorator @require_admin
        user = self.get_current_user()
        email = user['email']
        if (email != 'david810@gmail.com' and email != 'dbieber@princeton.edu'):
            self.redirect('/')
            return

        self.render('thyme/barchart.html', {
            'data_source': '/thyme/by_day/data.csv'
        })


class ThymeByDayDataHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self):
        # TODO(Bieber): Move this into a decorator @require_admin
        user = self.get_current_user()
        email = user['email']
        if (email != 'david810@gmail.com' and email != 'dbieber@princeton.edu'):
            self.redirect('/')
            return


        loader = TransactionLoader(use_dropbox=True)
        now = datetime.now()

        data = defaultdict(lambda: 0)
        for transaction in loader.transactions:
            transaction_datetime = transaction.get_datetime()
            day = transaction_datetime.date().isoformat()
            data[day] += -transaction.get_net_delta()

        self.writeln('name,value')
        for day in data:
            self.writeln('{0},{1}'.format(day, data[day]))


class ThymeByResourceHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self):
        # TODO(Bieber): Move this into a decorator @require_admin
        user = self.get_current_user()
        email = user['email']
        if (email != 'david810@gmail.com' and email != 'dbieber@princeton.edu'):
            self.redirect('/')
            return

        self.render('thyme/barchart.html', {
            'data_source': '/thyme/by_resource/data.csv'
        })


class ThymeByResourceDataHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self):
        # TODO(Bieber): Move this into a decorator @require_admin
        user = self.get_current_user()
        email = user['email']
        if (email != 'david810@gmail.com' and email != 'dbieber@princeton.edu'):
            self.redirect('/')
            return


        loader = TransactionLoader(use_dropbox=True)
        now = datetime.now()

        data = defaultdict(lambda: 0)
        for transaction in loader.transactions:
            resource = transaction.get_resource()
            delta = -transaction.get_net_delta()
            if delta >= 0:
                data[resource] += -transaction.get_net_delta()

        self.writeln('name,value')
        for resource in data:
            self.writeln('{0},{1}'.format(resource, data[resource]))


handlers = [
    (r'/thyme/by_resource/data\.csv', ThymeByResourceDataHandler),
    (r'/thyme/by_resource/?', ThymeByResourceHandler),
    (r'/thyme/by_day/data\.csv', ThymeByDayDataHandler),
    (r'/thyme/by_day/?', ThymeByDayHandler),
    (r'/thyme/?', ThymeHandler),
]
