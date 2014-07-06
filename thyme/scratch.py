from transactions import TransactionLoader
from transactions import TransactionAccumulator

loader = TransactionLoader(use_dropbox=False)
accumulator = TransactionAccumulator()
for transaction in loader.transactions:
    accumulator.handle_transaction(transaction)
    balance = accumulator.get_balance()
    print "%-40s %.2f" % (transaction, balance)

print "Balance:", accumulator.get_balance()
print "Delta:", accumulator.get_delta()
