from __future__ import absolute_import

import tornado.web

from collections import defaultdict
from datetime import date
from datetime import datetime
from datetime import timedelta

from auth.decorators import require_admin
from common.common import BaseHandler
from common.common import dumps
from thyme.alerts import CustomAlerts
from thyme.transactions import Transaction
from thyme.transactions import TransactionLoader
from thyme.transactions import TransactionAccumulator

OFFLINE = False

class SimpleHandler(BaseHandler):

    @require_admin
    def get(self):

        loader = TransactionLoader(use_dropbox=not OFFLINE)
        accumulator = TransactionAccumulator()

        start_of_day = datetime.fromordinal(date.today().toordinal())
        spent_today = 0
        for transaction in loader.transactions:
            accumulator.handle_transaction(transaction)
            if transaction.get_datetime() >= start_of_day and transaction.counts_as_expense():
                spent_today += transaction.get_net_delta()


        self.render('thyme/dashboard.html', {
            'arrangement': 'thyme/simple.jsx',
            'data': {
                'spent_today': spent_today,
                'cash': accumulator.get_balance('cash') or 0,
                'change': accumulator.get_balance('change') or 0,
            }
        })

class ThymeSimpleViewHandler(BaseHandler):

    @require_admin
    def get(self):
        loader = TransactionLoader(use_dropbox=not OFFLINE)
        accumulator = TransactionAccumulator()

        start_of_day = datetime.fromordinal(date.today().toordinal())
        spent_today = 0
        for transaction in loader.transactions:
            accumulator.handle_transaction(transaction)
            if transaction.get_datetime() >= start_of_day and transaction.counts_as_expense():
                spent_today += transaction.get_net_delta()

        self.writeln('<pre>')
        self.writeln('${:3.2f} spent today. <br/>'.format(spent_today))
        self.writeln('${:3.2f} in your pocket. <br/>'.format(accumulator.get_balance('cash') or 0))
        self.writeln('${:3.2f} on your desk. <br/>'.format(accumulator.get_balance('change') or 0))
        self.writeln('</pre>')

class ThymeErrorsViewHandler(BaseHandler):

    @require_admin
    def get(self):
        loader = TransactionLoader(use_dropbox=not OFFLINE)
        accumulator = TransactionAccumulator()

        self.writeln('<pre>Errors')

        for transaction in loader.transactions:
            if transaction.transaction_type == Transaction.BALANCE_REPORT:
                for resource, balance in transaction.get_balances():
                    previous_balance = accumulator.get_balance(resource)
                    if previous_balance is None:
                        continue

                    previous_balance = round(previous_balance, 4)
                    balance = round(balance, 4)
                    if previous_balance != balance:
                        self.writeln("{:18s}: {} BALANCE {} (previously {}; difference is {:+.2f})".format(
                            transaction.timestamp,
                            resource,
                            balance,
                            previous_balance,
                            round(balance - previous_balance, 4)
                        ))
            accumulator.handle_transaction(transaction)

        self.writeln('</pre>')

class ThymeAlertsViewHandler(BaseHandler):

    @require_admin
    def get(self):
        loader = TransactionLoader(use_dropbox=not OFFLINE)
        accumulator = TransactionAccumulator()

        for transaction in loader.transactions:
            accumulator.handle_transaction(transaction)

        alert_suite = CustomAlerts(loader, accumulator)
        alerts = alert_suite.check_for_alerts()

        self.writeln('<pre>')
        if alerts:
            for alert in alerts:
                self.writeln(alert)
        else:
            self.writeln("No alerts! Hurrah!")
        self.writeln('</pre>')

class ThymeUnhandledTransactionsViewHandler(BaseHandler):

    @require_admin
    def get(self):
        loader = TransactionLoader(use_dropbox=not OFFLINE)
        accumulator = TransactionAccumulator()

        self.writeln('<pre>Unhandled Transactions')

        no_unhandled_transactions = True
        for transaction in loader.transactions:
            accumulator.handle_transaction(transaction)
            if transaction.transaction_type == None:
                no_unhandled_transactions = False
                self.writeln(str(transaction))

        if no_unhandled_transactions:
            self.writeln('None')

        self.writeln('</pre>')


class ThymeBalanceByResourceViewHandler(BaseHandler):

    @require_admin
    def get(self):
        loader = TransactionLoader(use_dropbox=not OFFLINE)
        accumulator = TransactionAccumulator()

        for transaction in loader.transactions:
            accumulator.handle_transaction(transaction)

        self.writeln('<pre>')
        for resource in accumulator.get_resources():
            amount = accumulator.get_balance(resource)
            if amount:
                self.writeln('  ${:>10.2f} in {}.'.format(amount, resource))
        self.writeln('= ${:10.2f} total.'.format(accumulator.get_balance(), resource))
        self.writeln('</pre>')


class ThymeLogViewHandler(BaseHandler):

    @require_admin
    def get(self):
        loader = TransactionLoader(use_dropbox=not OFFLINE)
        accumulator = TransactionAccumulator()

        threshold_datetime = datetime.now() - timedelta(days=999)

        self.write('<pre>')
        total_expenses = 0.0
        for transaction in loader.transactions:
            if transaction.get_datetime() >= threshold_datetime:
                if transaction.counts_as_expense():
                    total_expenses += -transaction.get_net_delta()
                accumulator.handle_transaction(transaction)
                delta = transaction.get_net_delta()
                balance = accumulator.get_delta()
                self.write('%-40s %.2f (%.2f) <br/>' % (transaction, balance, delta))

        self.write('Balance: %.2f<br/>' % accumulator.get_balance())
        self.write('Delta: %.2f<br/>' % accumulator.get_delta())
        elapsed_time = accumulator.last_datetime - accumulator.first_datetime
        elapsed_days = (elapsed_time.total_seconds() / timedelta(days=1).total_seconds())

        self.write('Days: %.2f<br/>' % elapsed_days)
        self.write('NetRate: %.2f per day<br/>' % (accumulator.get_delta() / elapsed_days))
        self.write('OutRate: %.2f per day<br/>' % (total_expenses / elapsed_days))
        self.write('In pocket: %.2f<br/>' % accumulator.get_balance('cash'))
        self.write('</pre>')


class ThymeByDayHandler(BaseHandler):

    @require_admin
    def get(self):
        self.render('thyme/barchart.html', {
            'data_source': '/thyme/by_day/data.csv'
        })


class ThymeByDayDataHandler(BaseHandler):

    @require_admin
    def get(self):
        loader = TransactionLoader(use_dropbox=not OFFLINE)
        accumulator = TransactionAccumulator()

        data = defaultdict(lambda: 0)
        for transaction in loader.transactions:
            accumulator.handle_transaction(transaction)

            if transaction.counts_as_expense():
                transaction_datetime = transaction.get_datetime()
                day = transaction_datetime.date().isoformat()
                data[day] += -transaction.get_net_delta()

        self.writeln('name,value')
        date = accumulator.last_datetime.date()
        while date >= accumulator.first_datetime.date():
            day = date.isoformat()
            self.writeln('{0},{1}'.format(day, data[day]))
            date -= timedelta(days=1)


class ThymeByResourceHandler(BaseHandler):

    @require_admin
    def get(self):
        self.render('thyme/barchart.html', {
            'data_source': '/thyme/by_resource/data.csv'
        })


class ThymeByResourceDataHandler(BaseHandler):

    @require_admin
    def get(self):
        loader = TransactionLoader(use_dropbox=not OFFLINE)
        now = datetime.now()

        data = defaultdict(lambda: 0)
        for transaction in loader.transactions:
            resource = transaction.get_resource()
            delta = -transaction.get_net_delta()
            if delta >= 0 and resource is not None and transaction.counts_as_expense():
                data[resource] += -transaction.get_net_delta()

        self.writeln('name,value')
        for resource in data:
            self.writeln('{0},{1}'.format(resource, data[resource]))

class ThymeByDayOfWeekHandler(BaseHandler):

    @require_admin
    def get(self):
        self.render('thyme/barchart.html', {
            'data_source': '/thyme/by_day_of_week/data.csv'
        })


class ThymeByDayOfWeekDataHandler(BaseHandler):

    @require_admin
    def get(self):
        loader = TransactionLoader(use_dropbox=not OFFLINE)
        now = datetime.now()

        data = defaultdict(lambda: 0)
        for transaction in loader.transactions:
            if transaction.counts_as_expense():
                transaction_datetime = transaction.get_datetime()
                day = transaction_datetime.weekday()
                data[day] += -transaction.get_net_delta()


        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        self.writeln('name,value')
        for day in data:
            self.writeln('{0},{1}'.format(days[day], data[day]))


class ThymeByTimeHandler(BaseHandler):

    @require_admin
    def get(self):
        self.render('thyme/barchart.html', {
            'data_source': '/thyme/by_time/data.csv'
        })


class ThymeByTimeDataHandler(BaseHandler):

    @require_admin
    def get(self):
        loader = TransactionLoader(use_dropbox=not OFFLINE)
        now = datetime.now()

        data = defaultdict(lambda: 0)
        for transaction in loader.transactions:
            if transaction.counts_as_expense():
                transaction_datetime = transaction.get_datetime()
                hour = transaction_datetime.hour
                data[hour] += -transaction.get_net_delta()

        self.writeln('name,value')
        for hour in range(24):
            self.writeln('{0:02d},{1}'.format(hour, data[hour]))


class ThymeLineChartByDateHandler(BaseHandler):

    @require_admin
    def get(self):
        self.render('thyme/lineplot.html', {
            'data_source': '/thyme/line_chart/data.csv'
        })


class ThymeLineChartByDateDataHandler(BaseHandler):

    @require_admin
    def get(self):
        loader = TransactionLoader(use_dropbox=not OFFLINE)
        now = datetime.now()

        self.writeln('date,balance')
        accumulator = TransactionAccumulator()
        for transaction in loader.transactions:
            include_transaction = datetime.now() - transaction.get_datetime() <= timedelta(days=30)
            include_transaction &= len(accumulator.get_resources()) >= 5
            if include_transaction:
                self.writeln('{0},{1}'.format(
                    transaction.get_datetime(),
                    accumulator.get_balance(),
                ))

            accumulator.handle_transaction(transaction)

            if include_transaction:
                self.writeln('{0},{1}'.format(
                    transaction.get_datetime(),
                    accumulator.get_balance(),
                ))


class ThymeExpensesLineChartByDateHandler(BaseHandler):

    @require_admin
    def get(self):
        self.render('thyme/lineplot.html', {
            'data_source': '/thyme/expenses_line_chart/data.csv'
        })


class ThymeExpensesLineChartByDateDataHandler(BaseHandler):

    @require_admin
    def get(self):
        loader = TransactionLoader(use_dropbox=not OFFLINE)
        now = datetime.now()

        self.writeln('date,balance')
        accumulator = TransactionAccumulator()
        total_expenses = 0
        for transaction in loader.transactions:
            include_transaction = datetime.now() - transaction.get_datetime() <= timedelta(days=60)
            include_transaction &= len(accumulator.get_resources()) >= 5
            include_transaction &= transaction.counts_as_expense()
            if include_transaction:
                self.writeln('{0},{1}'.format(
                    transaction.get_datetime(),
                    total_expenses,
                ))
                total_expenses += transaction.get_net_delta()

            accumulator.handle_transaction(transaction)

            if include_transaction:
                self.writeln('{0},{1}'.format(
                    transaction.get_datetime(),
                    total_expenses,
                ))


class TestHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self):
        self.render("react_test.html", {
            "data": [1, 2, 3]
        })


class ThymeWeeklyComparisonHandler(BaseHandler):

    @require_admin
    def get(self):
        loader = TransactionLoader(use_dropbox=not OFFLINE)
        now = datetime.now()
        start_of_day = datetime.fromordinal(date.today().toordinal())

        interval = timedelta(days=7)
        start_of_interval = start_of_day - timedelta(days=start_of_day.weekday())

        end_of_interval = start_of_interval + interval
        start_of_last_interval = start_of_interval - interval

        interval_data = defaultdict(lambda: [(0,0)])
        interval_expenses = defaultdict(lambda: 0)

        # Now calculate intervals' expenses
        for transaction in loader.transactions:
            transaction_datetime = transaction.get_datetime()
            until_end_of_interval = end_of_interval - transaction_datetime
            intervals_ago = int(until_end_of_interval.total_seconds() / interval.total_seconds())

            start_of_old_interval = start_of_interval - interval*intervals_ago
            time_in_interval = transaction_datetime - start_of_old_interval

            if transaction.counts_as_expense():
                interval_data[intervals_ago].append((time_in_interval, interval_expenses[intervals_ago]))
                interval_expenses[intervals_ago] += transaction.get_net_delta()
                interval_data[intervals_ago].append((time_in_interval, interval_expenses[intervals_ago]))

        # Previous intervals are over, and this interval is up to now.
        interval_data[0].append((now - start_of_interval, interval_expenses[0]))
        for intervals_ago in interval_data:
            if intervals_ago != 0:
                interval_data[intervals_ago].append((interval, interval_expenses[intervals_ago]))

        # TODO(Bieber): Don't go back in time forever
        self.render("thyme/weekly_comparison.html", {
            "data": dumps(interval_data)
        })

class ThymeIndexViewHandler(BaseHandler):

    @require_admin
    def get(self):
        self.writeln('<pre>')
        for regex_str, handler in handlers:
            if "." in regex_str:  # don't link to data
                continue
            url = regex_str.replace('?', '')
            self.writeln('<a href="{}">{}</a>'.format(
                url, url
            ))
        self.writeln('</pre>')

class ThymeDerivativesViewHandler(BaseHandler):

    @require_admin
    def get(self):
        SECONDS_IN_A_DAY = 60 * 60 * 24
        loader = TransactionLoader(use_dropbox=not OFFLINE)
        now = datetime.now()
        # TODO(Bieber): Use linear kernal
        interval = timedelta(days=14)  # derivative[m] = (value[m] - value[m - interval]) / interval
        start_datetime = now - timedelta(days=60)

        deltas = []
        for transaction in loader.transactions:
            # TODO(Bieber): Right now the data source is providing sorted transactions
            # but we may need a stronger guarantee of chronological order
            net_delta = transaction.get_net_delta()
            transaction_datetime = transaction.get_datetime()
            if transaction.counts_as_expense():
                deltas.append((transaction_datetime, net_delta))
                deltas.append((transaction_datetime + interval, -net_delta))
        deltas = sorted(deltas, key=lambda d: d[0])

        data = []
        derivative = 0
        for delta_datetime, delta in deltas:
            include_in_data = delta_datetime < now and delta_datetime >= start_datetime
            if include_in_data:
                data.append((delta_datetime - start_datetime, derivative))
            if delta_datetime < now:
                derivative += delta / (interval.total_seconds() / SECONDS_IN_A_DAY)
            if include_in_data:
                data.append((delta_datetime - start_datetime, derivative))
        data.append((now - start_datetime, derivative))

        self.render("thyme/weekly_comparison.html", {
            "data": dumps([data])
        })


class ThymeRecentTransactionsViewHandler(BaseHandler):

    @require_admin
    def get(self):
        # TODO(Bieber): Implement ThymeRecentTransactionsViewHandler
        self.writeln("Not implemented yet")

handlers = [
    (r'/thyme/test_endpoint/?', TestHandler),

    (r'/thyme/weekly_comparison/?', ThymeWeeklyComparisonHandler),

    (r'/thyme/simple2/?', SimpleHandler),
    (r'/thyme/simple/?', ThymeSimpleViewHandler),
    (r'/thyme/errors/?', ThymeErrorsViewHandler),
    (r'/thyme/alerts/?', ThymeAlertsViewHandler),
    (r'/thyme/derivatives/?', ThymeDerivativesViewHandler),
    (r'/thyme/unhandled_transactions/?', ThymeUnhandledTransactionsViewHandler),
    (r'/thyme/balance_by_resource/?', ThymeBalanceByResourceViewHandler),
    (r'/thyme/line_chart/data\.csv', ThymeLineChartByDateDataHandler),
    (r'/thyme/line_chart/?', ThymeLineChartByDateHandler),
    (r'/thyme/expenses_line_chart/data\.csv', ThymeExpensesLineChartByDateDataHandler),
    (r'/thyme/expenses_line_chart/?', ThymeExpensesLineChartByDateHandler),
    (r'/thyme/by_day_of_week/data\.csv', ThymeByDayOfWeekDataHandler),
    (r'/thyme/by_day_of_week/?', ThymeByDayOfWeekHandler),
    (r'/thyme/by_time/data\.csv', ThymeByTimeDataHandler),
    (r'/thyme/by_time/?', ThymeByTimeHandler),
    (r'/thyme/by_resource/data\.csv', ThymeByResourceDataHandler),
    (r'/thyme/by_resource/?', ThymeByResourceHandler),
    (r'/thyme/by_day/data\.csv', ThymeByDayDataHandler),
    (r'/thyme/by_day/?', ThymeByDayHandler),
    (r'/thyme/log_view/?', ThymeLogViewHandler),
    (r'/thyme/?', ThymeIndexViewHandler),
]
