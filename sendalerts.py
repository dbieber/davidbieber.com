from __future__ import absolute_import

from sendlater.mailer import Mailer
from settings import settings
from thyme.alerts import CustomAlerts
from thyme.alerts import BookAlerts
from thyme.booklogs import BookLogLoader
from thyme.booklogs import BookLogAccumulator
from thyme.transactions import TransactionAccumulator
from thyme.transactions import TransactionLoader

OFFLINE = False  # TODO(Bieber): Move to settings

def main():
    mailer = Mailer()
    mailer.login(settings.secure.GMAIL_USER, settings.secure.GMAIL_PASSWD)

    # Financial Alerts
    loader = TransactionLoader(use_dropbox=not OFFLINE)
    accumulator = TransactionAccumulator()
    for transaction in loader.transactions:
        accumulator.handle_transaction(transaction)
    alert_suite = CustomAlerts(loader, accumulator)
    alerts = alert_suite.check_for_alerts()

    print alerts

    if alerts:
        message = '  '.join(alert[0] for alert in alerts)
        mailer.unix_mail(
            user='alerts',
            to=settings.secure.ALERTS_RECIPIENT,
            subject='Thyme',
            text=message,
        )

    # Book Alerts
    loader = BookLogLoader(use_dropbox=True)
    accumulator = BookLogAccumulator()
    for log in loader.logs:
        accumulator.handle_log(log)
    alert_suite = BookAlerts(loader, accumulator)
    alerts = alert_suite.check_for_alerts()

    print alerts

    if alerts:
        message = '  '.join(alert[0] for alert in alerts)
        mailer.unix_mail(
            user='alerts',
            to=settings.secure.ALERTS_RECIPIENT,
            subject='Bach',
            text=message,
        )

if __name__ == '__main__':
    main()

