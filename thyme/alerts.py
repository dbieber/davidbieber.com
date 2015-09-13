from __future__ import absolute_import

from collections import defaultdict
from datetime import date
from datetime import datetime
from datetime import timedelta
from math import ceil

from thyme.transactions import Transaction

class AlertSuite():

    def __init__(self, loader, accumulator):
        self.alerts = []
        self.accumulator = accumulator
        self.loader = loader

    def alert(self, *alerts):
        self.alerts.append(alerts)

    def check_for_alerts(self):
        for attribute in dir(self):
            if 'alert' in attribute and attribute not in ['alert', 'alerts', 'check_for_alerts']:
                alert_function = getattr(self, attribute)
                alert_function()

        return self.alerts

    def get_recent_trasactions(self, delta):
        # TODO(Bieber): This could be more efficient
        threshold_datetime = datetime.now() - delta
        return list(filter(lambda t: t.get_datetime() >= threshold_datetime, self.loader.transactions))

    def get_balance(self, resource):
        return self.accumulator.get_balance(resource)

class CustomAlerts(AlertSuite):

    def challah_alert(self):
        # Challah Alert: If you haven't purchased challah for Friday night,
        # this alert is triggered
        today = date.today()
        if today.weekday() in [3, 4]:  # Thursday or Friday:
            purchased_challah = False
            for transaction in self.get_recent_trasactions(timedelta(days=3)):
                if 'challah' in transaction.description.lower():
                    purchased_challah = True
            if not purchased_challah:
                self.alert("You haven't purchased challah for Shabbat yet.")

    def low_funds_alerts(self):
        # TODO(Bieber): Load minimum balances from a config or database
        if self.get_balance('cash') < 25:
            self.alert('You have less than $25.00 in cash.')

        if self.get_balance('change') > 5:
            self.alert('You have more than $5.00 in change.')

        if self.get_balance('credit') < 5000:
            self.alert('You have less than $5000.00 in credit.')

        if self.get_balance('credit') < 1000:
            self.alert('You have less than $1000.00 in credit (${}).'.format(self.get_balance('credit')))

    def no_recent_balance_report_alerts(self):
        # Balance report alert: If you haven't entered your balance for a resource
        # recently, this alert is triggered.
        reports_needed = {
            'cash': timedelta(days=7),
            'credit': timedelta(days=7),
            'savings': timedelta(days=14),
            'venmo': timedelta(days=7),
            'paypal': timedelta(days=30),
            'change': timedelta(days=30),
            'discovercd-729': timedelta(days=90),
            'accounta': timedelta(days=90),
            'accountb': timedelta(days=90),
        }

        now = datetime.now()
        largest_delta = max(reports_needed[resource] for resource in reports_needed)
        last_report_timedeltas = defaultdict(lambda: largest_delta)
        for transaction in self.get_recent_trasactions(largest_delta):
            if transaction.transaction_type == Transaction.BALANCE_REPORT:
                resource = transaction.get_resource()
                transaction_datetime = transaction.get_datetime()
                report_timedelta = now - transaction_datetime
                last_report_timedeltas[resource] = min(last_report_timedeltas[resource], report_timedelta)
                if resource in reports_needed and report_timedelta < reports_needed[resource]:
                    del reports_needed[resource]

        for resource in reports_needed:
            self.alert(
                "You haven't entered a {resource} balance report in over {days} days.".format(
                    resource=resource.upper(),
                    days=last_report_timedeltas[resource].days,
                )
            )

    def no_activity_alerts(self):
        # TODO(Bieber): Create alert for if no transactions have been posted in X days
        # TODO(Bieber): Create alert for if the alerts page hasn't been viewed in X days
        # TODO(Bieber): Create alert for if a TODO has sat unchanged for X days
        pass

class BookAlerts(AlertSuite):

    def insufficient_reading_alerts(self):
        today = date.today()
        start_of_year = date(today.year, 1, 1)
        time_passed = today - start_of_year
        days_passed = time_passed.days + 1  # include today
        dates_read = list(filter(lambda d: d >= start_of_year, self.accumulator.dates_read))
        ratio_read = float(len(dates_read)) / days_passed
        desired_ratio = 200.0 / 365
        if ratio_read * 365 < 200:
            self.alert(
                "At this rate you'll read only {days} days this year.".format(
                    days=ratio_read * 365,
                )
            )

        if today.day == 4:  # the fourth of every month
            self.alert(
                "You've read {days} days so far out of {total_days} total days this year.".format(
                    days=len(dates_read),
                    total_days=days_passed,
                )
            )

        consecutive_days_to_read = ceil((200.0/365 * days_passed - len(dates_read)) / (1 - desired_ratio))
        if consecutive_days_to_read > 0:
            self.alert(
                "Try to read {days} consecutive days to get up to speed.".format(
                    days=consecutive_days_to_read,
                )
            )
        else:
            pass
            # self.alert("You could forget to read {} consecutive days and be O.K.".format(-consecutive_days_to_read))

        seven_days_ago = today - timedelta(days=7)
        dates_read = list(filter(lambda d: d > seven_days_ago, self.accumulator.dates_read))
        ratio_read = float(len(dates_read)) / 7.0
        # self.alert("You read {} days in the last week.".format(len(dates_read)))

        days_not_read = 0
        date_not_read = today
        while date_not_read not in self.accumulator.dates_read:
            days_not_read += 1
            date_not_read -= timedelta(days=1)

        if days_not_read == 1:
            self.alert("You haven't read today.".format(days_not_read))
        elif days_not_read == 2:
            self.alert("You haven't read in over a day.".format(days_not_read))
        elif days_not_read > 2:
            self.alert(
                "You haven't read in over {days} days.".format(
                    days=days_not_read - 1,
                )
            )
