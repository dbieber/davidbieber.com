from datetime import datetime
from datetime import timedelta

from transactions import TransactionLoader
from transactions import TransactionAccumulator

loader = TransactionLoader(use_dropbox=True)
accumulator = TransactionAccumulator(drop_change=True)

threshold_datetime = datetime.now() - timedelta(days=999)

for transaction in loader.transactions:
    if transaction.get_datetime() >= threshold_datetime:
        accumulator.handle_transaction(transaction)
        delta = transaction.get_net_delta()
        balance = accumulator.get_delta()
        print "%-40s %.2f (%.2f)" % (transaction, balance, delta)

print "Balance:", accumulator.get_balance()
print "Delta:", accumulator.get_delta()
elapsed_time = accumulator.last_datetime - accumulator.first_datetime
elapsed_days = (elapsed_time.total_seconds() / timedelta(days=1).total_seconds())
print "Days: %.2f" % elapsed_days
print "Rate: %.2f per day" % (accumulator.get_delta() / elapsed_days)
print "In pocket: %.2f" % accumulator.get_balance('cash')
