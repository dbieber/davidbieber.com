from transactions import TransactionLoader
from transactions import TransactionAccumulator

loader = TransactionLoader(use_dropbox=False)
accumulator = TransactionAccumulator(drop_change=True)
for transaction in loader.transactions:
    accumulator.handle_transaction(transaction)
    delta = transaction.get_net_delta()
    balance = accumulator.get_delta()
    print "%-40s %.2f (%.2f)" % (transaction, balance, delta)

print "Balance:", accumulator.get_balance()
print "Delta:", accumulator.get_delta()
