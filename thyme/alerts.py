from __future__ import absolute_import

from datetime import date
from datetime import datetime
from datetime import timedelta

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
        threhold_datetime = datetime.now() - delta
        return filter(lambda t: t.get_datetime() >= threhold_datetime, self.loader.transactions)

    def get_balance(self, resource):
        return self.accumulator.get_balance(resource)

class CustomAlerts(AlertSuite):

    def challah_alert(self):
        # Challah Alert: If you haven't purchased challah for Friday night,
        # this alert is triggered
        today = date.today()
        if today.weekday() in [4, 5]:  # Friday or Saturday:
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

    def no_recent_balance_report_alerts(self):
        # Balance report alert: If you haven't entered your balance for a resource
        # recently, this alert is triggered.
        reports_needed = {
            'cash': timedelta(days=7),
            'credit': timedelta(days=7),
            'savings': timedelta(days=14),
            'venmo': timedelta(days=7),
            'paypal': timedelta(days=30),
            'change': timedelta(days=14),
        }

        now = datetime.now()
        largest_delta = max(reports_needed[resource] for resource in reports_needed)
        for transaction in self.get_recent_trasactions(largest_delta):
            if transaction.transaction_type == Transaction.BALANCE_REPORT:
                resource = transaction.get_resource()
                transaction_datetime = transaction.get_datetime()
                if resource in reports_needed and now - transaction_datetime < reports_needed[resource]:
                    del reports_needed[resource]

        for resource in reports_needed:
            self.alert("You haven't entered a {} balance report in over {} days".format(
                resource.upper(), reports_needed[resource].days
            ))

    def no_activity_alerts(self):
        # TODO(Bieber): Create alert for if no transactions have been posted in X days
        # TODO(Bieber): Create alert for if the alerts page hasn't been viewed in X days
        # TODO(Bieber): Create alert for if a TODO has sat unchanged for X days
        pass
