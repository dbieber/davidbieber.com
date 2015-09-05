from __future__ import absolute_import

import locale
import tornado.web

from collections import defaultdict
from datetime import date
from datetime import datetime
from datetime import timedelta
from terminaltables import AsciiTable
from textwrap import wrap

from auth.decorators import require_admin
from common.common import BaseHandler
from common.common import dumps
from thyme.alerts import BookAlerts
from thyme.alerts import CustomAlerts
from thyme.booklogs import BookLogAccumulator
from thyme.booklogs import BookLogLoader
from thyme.categorizer import get_categories
from thyme.categorizer import subcategories
from thyme.transactions import Transaction
from thyme.transactions import TransactionAccumulator
from thyme.transactions import TransactionLoader
from thyme.utils import category_as_link

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

def get_fn_accum(ts, fn):
    accumulator = TransactionAccumulator()
    for t in ts:
        if fn(t):
            accumulator.handle_transaction(t)
    return accumulator

def get_expense_accum(ts, n):
    accumulator = TransactionAccumulator()
    for t in ts:
        d = t.get_net_delta()
        if abs(d) <= n and d < 0:
            accumulator.handle_transaction(t)
    return accumulator

def get_income_accum(ts, n):
    accumulator = TransactionAccumulator()
    for t in ts:
        d = t.get_net_delta()
        if abs(d) <= n and d > 0:
            accumulator.handle_transaction(t)
    return accumulator

class ThymeStatsViewHandler(BaseHandler):

    @require_admin
    def get(self):
        loader = TransactionLoader(use_dropbox=not OFFLINE)

        expense_accumulator = get_expense_accum(loader.transactions, 9999999)
        income_accumulator = get_income_accum(loader.transactions, 9999999)

        for threshold in [10, 100, 1000]:

            minor_expense_accumulator = get_fn_accum(
                loader.transactions,
                lambda t: -t.get_net_delta() < threshold and t.get_net_delta() < 0,
            )
            major_expense_accumulator = get_fn_accum(
                loader.transactions,
                lambda t: -t.get_net_delta() >= threshold and t.get_net_delta() < 0,
            )

            minor_income_accumulator = get_fn_accum(
                loader.transactions,
                lambda t: t.get_net_delta() < threshold and t.get_net_delta() > 0,
            )
            major_income_accumulator = get_fn_accum(
                loader.transactions,
                lambda t: t.get_net_delta() >= threshold and t.get_net_delta() > 0,
            )

            self.writeln('''<pre>
                # expenses: {num_expenses:5d} (${total_cost:8.2f})
                #  incomes: {num_incomes:5d} (${total_income:8.2f})

          # minor expenses: {num_minor_expenses:5d} (${total_minor_expenses:8.2f})
          # major expenses: {num_major_expenses:5d} (${total_major_expenses:8.2f})

           # minor incomes: {num_minor_incomes:5d} (${total_minor_incomes:8.2f})
           # major incomes: {num_major_incomes:5d} (${total_major_incomes:8.2f})

                 Threshold: {threshold:5d}
            </pre>'''.format(
                num_expenses=expense_accumulator.count,
                total_cost=-expense_accumulator.get_delta(),
                num_incomes=income_accumulator.count,
                total_income=income_accumulator.get_delta(),
                num_minor_expenses=minor_expense_accumulator.count,
                total_minor_expenses=minor_expense_accumulator.get_delta(),
                num_major_expenses=major_expense_accumulator.count,
                total_major_expenses=major_expense_accumulator.get_delta(),
                num_minor_incomes=minor_income_accumulator.count,
                total_minor_incomes=minor_income_accumulator.get_delta(),
                num_major_incomes=major_income_accumulator.count,
                total_major_incomes=major_income_accumulator.get_delta(),
                threshold=threshold,
            ))

class ThymeErrorsViewHandler(BaseHandler):

    @require_admin
    def get(self):
        loader = TransactionLoader(use_dropbox=not OFFLINE)
        accumulator = TransactionAccumulator()

        total_error = 0
        total_diff = 0

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
                            round(balance - previous_balance, 4),
                        ))

                        total_error += abs(round(balance - previous_balance, 4))
                        total_diff += round(balance - previous_balance, 4)
            accumulator.handle_transaction(transaction)

        self.writeln('Total error: {}'.format(total_error))
        self.writeln(' Total diff: {}'.format(total_diff))

        self.writeln('</pre>')

class BookProgressViewHandler(BaseHandler):

    @require_admin
    def get(self):
        loader = BookLogLoader(use_dropbox=True)
        accumulator = BookLogAccumulator()
        for log in loader.logs:
            accumulator.handle_log(log)

        def sanitize(value, width):
            rows = []
            for row in value.split('\n'):
                row = '\n'.join(wrap(row, width))
                rows.append(row)
            return '\n'.join(rows)

        def timestamp(x):
            book_id, record = x
            return datetime.strptime(record.last_updated, '%m/%d/%y, %I:%M %p')

        items = [['', 'ID', 'title', 'author', 'progress', 'notes']]
        widths = [17, 30, 30, 30, 30, 70]
        for book_id, book_record in sorted(accumulator.book_records.items(), key=timestamp, reverse=True):
            item = [
                book_record.last_updated or '',
                book_id,
                book_record.title or '',
                book_record.author or '',
                ', '.join(book_record.progress),
                '\n'.join("{:>17s}: {}".format(note[0], note[1]) for note in book_record.notes),
            ]
            item = [sanitize(value, width) for value, width in zip(item, widths)]
            items.append(item)
        table = AsciiTable(items)
        table.inner_row_border = True

        self.writeln('<pre>')
        self.writeln(
            table.table
        )
        self.writeln('</pre>')


class ThymeAlertsViewHandler(BaseHandler):

    @require_admin
    def get(self):
        loader = TransactionLoader(use_dropbox=not OFFLINE)
        accumulator = TransactionAccumulator()

        for transaction in loader.transactions:
            accumulator.handle_transaction(transaction)

        self.writeln('<pre>')

        alert_suite = CustomAlerts(loader, accumulator)
        alerts = alert_suite.check_for_alerts()

        if alerts:
            for alert in alerts:
                self.writeln(alert)
        else:
            self.writeln("No Thyme alerts! Hurrah!")

        loader = BookLogLoader(use_dropbox=True)
        accumulator = BookLogAccumulator()
        for log in loader.logs:
            accumulator.handle_log(log)
        alert_suite = BookAlerts(loader, accumulator)
        alerts = alert_suite.check_for_alerts()

        if alerts:
            for alert in alerts:
                self.writeln(alert)
        else:
            self.writeln("No Bach alerts! Hurrah!")

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


class ThymeBalanceReportsViewHandler(BaseHandler):

    @require_admin
    def get(self):
        loader = TransactionLoader(use_dropbox=not OFFLINE)
        accumulator = TransactionAccumulator()

        self.writeln('<pre>Balance Reports')

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
                    else:
                        self.writeln("{:18s}: {} BALANCE {}".format(
                            transaction.timestamp,
                            resource,
                            balance,
                        ))

            accumulator.handle_transaction(transaction)

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

class ThymeLogCategoryViewHandler(BaseHandler):

    @require_admin
    def get(self):
        loader = TransactionLoader(use_dropbox=not OFFLINE)
        accumulator = TransactionAccumulator()

        threshold_datetime = datetime.now() - timedelta(days=999)

        self.write('<pre>')
        for transaction in loader.transactions:
            if transaction.get_datetime() >= threshold_datetime:
                accumulator.handle_transaction(transaction)
                delta = transaction.get_net_delta()
                categories = get_categories(transaction.description)
                self.write('%-100s (%10.2f)   %s<br/>' % (transaction, delta, ' '.join(cat.upper() for cat in categories)))

        self.write('</pre>')

class ThymeCategoryViewHandler(BaseHandler):

    @require_admin
    def get(self):
        loader = TransactionLoader(use_dropbox=not OFFLINE)
        accumulator = TransactionAccumulator()

        threshold_datetime = datetime.now() - timedelta(days=999)

        category_totals = defaultdict(lambda: 0)

        all_subcategories = set()
        for supercategory, subcategory_list in subcategories.items():
            all_subcategories.update(subcategory_list)

        for transaction in loader.transactions:
            if transaction.get_datetime() >= threshold_datetime:
                accumulator.handle_transaction(transaction)
                delta = transaction.get_net_delta()
                categories = get_categories(transaction.description)

                if not categories:
                    categories = ['uncategorized']

                primary_categories = set(categories) - all_subcategories
                for category in categories:
                    category_totals[category] += delta / len(primary_categories)


        total_categorized_expenses = sum(
            category_totals[c]
            for c in category_totals
            if category_totals[c] < 0 and c not in all_subcategories
        )

        total_income = category_totals['income']

        self.write('<pre>')
        for category in sorted(set(category_totals.keys()) - all_subcategories, key=lambda c: category_totals[c]):
            self.writeln('{category_link} {amount:-15.2f}   {percent:7.2f}   {percent2:7.2f}'.format(
                category_link=category_as_link('{category:15s}'.format(category=category.upper())),
                amount=category_totals[category],
                percent=100 * category_totals[category] / total_categorized_expenses,
                percent2=abs(100 * category_totals[category] / total_income),
            ))
        self.writeln()

        for category in sorted(all_subcategories, key=lambda c: category_totals[c]):
            self.writeln('{category_link} {amount:-15.2f}   {percent:7.2f}   {percent2:7.2f}'.format(
                category_link=category_as_link('{category:15s}'.format(category=category.upper())),
                amount=category_totals[category],
                percent=100 * category_totals[category] / total_categorized_expenses,
                percent2=abs(100 * category_totals[category] / total_income),
            ))

        self.write('</pre>')

class ThymeWeekCategoryViewHandler(BaseHandler):

    @require_admin
    def get(self, week):
        loader = TransactionLoader(use_dropbox=not OFFLINE)
        accumulator = TransactionAccumulator()

        week = int(week)

        threshold_datetime = datetime.now() - timedelta(days=week)

        category_totals = defaultdict(lambda: 0)

        all_subcategories = set()
        for supercategory, subcategory_list in subcategories.items():
            all_subcategories.update(subcategory_list)

        for transaction in loader.transactions:
            if transaction.get_datetime() >= threshold_datetime:
                accumulator.handle_transaction(transaction)
                delta = transaction.get_net_delta()
                categories = get_categories(transaction.description)

                if not categories:
                    categories = ['uncategorized']

                primary_categories = set(categories) - all_subcategories
                for category in categories:
                    category_totals[category] += delta / len(primary_categories)


        total_categorized_expenses = sum(
            category_totals[c]
            for c in category_totals
            if category_totals[c] < 0 and c not in all_subcategories
        )

        total_income = category_totals['income'] or 99999999

        self.write('<pre>')
        for category in sorted(set(category_totals.keys()) - all_subcategories, key=lambda c: category_totals[c]):
            self.writeln('{category:15s} {amount:-15.2f}   {percent:7.2f}   {percent2:7.2f}'.format(
                category=category.upper(),
                amount=category_totals[category],
                percent=100 * category_totals[category] / total_categorized_expenses,
                percent2=abs(100 * category_totals[category] / total_income),
            ))
        self.writeln()

        for category in sorted(all_subcategories, key=lambda c: category_totals[c]):
            self.writeln('{category:15s} {amount:-15.2f}   {percent:7.2f}   {percent2:7.2f}'.format(
                category=category.upper(),
                amount=category_totals[category],
                percent=100 * category_totals[category] / total_categorized_expenses,
                percent2=abs(100 * category_totals[category] / total_income),
            ))

        self.write('</pre>')

class ThymeExpensesByCategoryViewHandler(BaseHandler):

    @require_admin
    def get(self, category):
        loader = TransactionLoader(use_dropbox=not OFFLINE)
        accumulator = TransactionAccumulator()

        self.write('<pre>')

        for transaction in loader.transactions:
            accumulator.handle_transaction(transaction)

            categories = get_categories(transaction.description)
            if category in categories or (category == 'uncategorized' and not categories):
                self.writeln(transaction)

        self.write('</pre>')

class ThymeUncategorizedViewHandler(BaseHandler):

    @require_admin
    def get(self):
        loader = TransactionLoader(use_dropbox=not OFFLINE)
        accumulator = TransactionAccumulator()

        threshold_datetime = datetime.now() - timedelta(days=999)

        self.write('<pre>')
        for transaction in loader.transactions:
            if transaction.get_datetime() >= threshold_datetime:
                accumulator.handle_transaction(transaction)
                delta = transaction.get_net_delta()
                categories = get_categories(transaction.description)

                if transaction.transaction_type in [Transaction.BALANCE_REPORT, Transaction.WITHDRAWAL, Transaction.TRANSFER]:
                    continue

                if not categories:
                    self.write('%-100s (%10.2f)<br/>' % (transaction, delta))
        self.write('</pre>')


class ThymeLogViewHandlerByAmount(BaseHandler):

    @require_admin
    def get(self):
        loader = TransactionLoader(use_dropbox=not OFFLINE)
        accumulator = TransactionAccumulator()

        threshold_datetime = datetime.now() - timedelta(days=999)

        self.write('<pre>')
        total_expenses = 0.0
        for transaction in sorted(loader.transactions, lambda s, t: 1 if t.get_net_delta() < s.get_net_delta() else -1):
            if transaction.get_datetime() >= threshold_datetime:
                if transaction.counts_as_expense():
                    total_expenses += -transaction.get_net_delta()
                accumulator.handle_transaction(transaction)
                delta = transaction.get_net_delta()
                balance = accumulator.get_delta()
                self.write('%-40s %.2f (%.2f) <br/>' % (transaction, balance, delta))
        self.write('</pre>')

class ThymeLogViewHandlerByDesc(BaseHandler):

    @require_admin
    def get(self):
        loader = TransactionLoader(use_dropbox=not OFFLINE)
        accumulator = TransactionAccumulator()

        threshold_datetime = datetime.now() - timedelta(days=999)

        self.write('<pre>')
        total_expenses = 0.0
        for transaction in sorted(loader.transactions, lambda s, t: 1 if t.description < s.description else -1):
            if transaction.get_datetime() >= threshold_datetime:
                if transaction.counts_as_expense():
                    total_expenses += -transaction.get_net_delta()
                accumulator.handle_transaction(transaction)
                delta = transaction.get_net_delta()
                balance = accumulator.get_delta()
                self.write('%-40s %.2f (%.2f) <br/>' % (transaction, balance, delta))
        self.write('</pre>')

class ThymeByDayHandler(BaseHandler):

    @require_admin
    def get(self):
        self.render('thyme/barchart.html', {
            'height': 15 * (datetime.now() - datetime(2014, 6, 14)).days,
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
            'data_source': '/thyme/by_day_of_week/data.csv',
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
            if '.' in regex_str:  # don't link to data
                continue
            if 'webhook' in regex_str:  # don't link to webhooks
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

class ThymePaypalWebhook(BaseHandler):

    def post(self):
        body = self.request.body
        filename = 'paypal-webhook-{}.post'.format(
            str(datetime.now()).replace(' ', '-').replace(':', '-').replace('.', '-')
        )
        with open(filename, 'w') as f:
            f.write(str(body))

    def check_xsrf_cookie(self):
        return True

handlers = [
    (r'/thyme/test_endpoint/?', TestHandler),

    (r'/thyme/weekly_comparison/?', ThymeWeeklyComparisonHandler),

    (r'/thyme/simple2/?', SimpleHandler),
    (r'/thyme/stats/?', ThymeStatsViewHandler),
    (r'/thyme/simple/?', ThymeSimpleViewHandler),
    (r'/thyme/errors/?', ThymeErrorsViewHandler),
    (r'/thyme/alerts/?', ThymeAlertsViewHandler),
    (r'/thyme/book_progress/?', BookProgressViewHandler),
    (r'/thyme/derivatives/?', ThymeDerivativesViewHandler),
    (r'/thyme/unhandled_transactions/?', ThymeUnhandledTransactionsViewHandler),
    (r'/thyme/balance_reports/?', ThymeBalanceReportsViewHandler),
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
    (r'/thyme/log_categories/?', ThymeLogCategoryViewHandler),
    (r'/thyme/categories/?', ThymeCategoryViewHandler),
    (r'/thyme/categories/(.*)?', ThymeWeekCategoryViewHandler),
    (r'/thyme/expenses_by_category/(.*)?', ThymeExpensesByCategoryViewHandler),
    (r'/thyme/uncategorized/?', ThymeUncategorizedViewHandler),
    (r'/thyme/log_view_amount/?', ThymeLogViewHandlerByAmount),
    (r'/thyme/log_view_description/?', ThymeLogViewHandlerByDesc),
    (r'/thyme/?', ThymeIndexViewHandler),

    (r'/thyme/paypal-webhook/?', ThymePaypalWebhook),
]
