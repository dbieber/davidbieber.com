from collections import defaultdict
from datetime import datetime

from transactions import TransactionLoader

import csv

resources = set()
resources.add('cash')
resources.add('credit')
resources.add('savings')
resources.add('paypal')
resources.add('venmo')
balances = defaultdict(lambda: 0)
deltas = defaultdict(lambda: 0)

DROP_CHANGE = True
lost_change = 0

def isAmount(s):
    try:
        amount(s)
        return True
    except ValueError:
        return False

def amount(s):
    s = s.replace('$', '')
    return float(s)

def hasSign(s):
    return s[0] == '+' or s[0] == '-'

def as_datetime(timestamp):
    DATETIME_FORMAT = '%m/%d/%y, %H:%M %p'
    return datetime.strptime(timestamp, DATETIME_FORMAT)

r = csv.reader(transactions_file, delimiter=',', quotechar='"')

first_datetime = None
last_datetime = None
for row in r:
    if len(row) != 2:
        continue
    timestamp, transaction = row
    transaction_datetime = as_datetime(timestamp)

    # Determine first and last transactions
    if first_datetime is None or transaction_datetime < first_datetime:
        first_datetime = transaction_datetime
    if last_datetime is None or transaction_datetime > last_datetime:
        last_datetime = transaction_datetime

    tokens = transaction.lower().strip().split(' ')
    if tokens[0] == 'withdraw':
        amt = amount(tokens[1])
        resource_from = tokens[3]
        resource_to = tokens[5]
        balances[resource_from] -= amt
        balances[resource_to] += amt
        deltas[resource_from] -= amt
        deltas[resource_to] += amt
        print '%s: %.2f' % (resource_from, balances[resource_from]), "(withdraw %.2f)" % (amt)
        print '%s: %.2f' % (resource_to, balances[resource_to]), "(%.2f from withdrawal)" % (amt)
    if tokens[0] in resources and isAmount(tokens[1]):
        amt = amount(tokens[1])
        if not hasSign(tokens[1]):
            amt *= -1
        resource = tokens[0]
        balances[resource] += amt
        deltas[resource] += amt
        description = ' '.join(tokens[2:])
        print resource+':', balances[resource], '(%.2f):' % amt, description
    elif tokens[0] in resources and tokens[1] == 'balance' and isAmount(tokens[2]):
        old_balance = balances[tokens[0]]
        balances[tokens[0]] = amount(tokens[2])
        print tokens[0]+':', balances[tokens[0]], 'balance', '(%.2f)' % (balances[tokens[0]] - old_balance)
    # resources.add(tokens[0])

    if DROP_CHANGE:
        if balances['cash'] != int(balances['cash']):
            old_balance = balances['cash']
            balances['cash'] = int(balances['cash'])
            lost_change += (balances[tokens[0]] - old_balance)
            print 'cash:', balances[tokens[0]], '(%.2f in lost change)' % (balances[tokens[0]] - old_balance)

print
total_balance = 0
total_delta = 0
for resource in resources:
    print "%s: %.2f (%.2f)" % (resource, balances[resource], deltas[resource])
    total_balance += balances[resource]
    total_delta += deltas[resource]

elapsed_time = last_datetime - first_datetime
print elapsed_time

print "Total: %.2f (%.2f)" % (total_balance, total_delta)
print "%.2f per day" % (total_delta / elapsed_time.days)
