from __future__ import absolute_import

from sendlater.mailer import Mailer
from settings import settings
from thyme.alerts import CustomAlerts
from thyme.transactions import TransactionAccumulator
from thyme.transactions import TransactionLoader

OFFLINE = False  # TODO(Bieber): Move to settings

def main():
    mailer = Mailer()
    mailer.login(settings.secure.GMAIL_USER, settings.secure.GMAIL_PASSWD)

    loader = TransactionLoader(use_dropbox=not OFFLINE)
    accumulator = TransactionAccumulator()

    for transaction in loader.transactions:
        accumulator.handle_transaction(transaction)

    alert_suite = CustomAlerts(loader, accumulator)
    alerts = alert_suite.check_for_alerts()

    if alerts:
        message = '  '.join(alert[0] for alert in alerts)
        mailer.mail(
            to=settings.secure.ALERTS_RECIPIENT,
            subject='Thyme Alerts',
            text=message,
        )

if __name__ == '__main__':
    main()

