from __future__ import absolute_import

from collections import defaultdict

import csv
import dropbox

from settings import settings
from thyme.utils import timestamp_as_datetime


class TransactionLoader(object):

    def __init__(self, use_dropbox=True, filenames=None):

        self.transactions = []

        possible_filenames = filenames or [
            '/Transactions 2014.csv',
            '/Transactions 2015.csv',
            '/Transactions 2016.csv',
            '/Transactions.csv',
        ]

        for filename in possible_filenames:
            try:
                if use_dropbox:
                    self.dropbox_client = dropbox.client.DropboxClient(settings.secure.access_token)

                    # TODO(Bieber): Cache the file
                    transactions_file, metadata = self.dropbox_client.get_file_and_metadata(filename)
                else:
                    transactions_file = open(filename, 'r')
            except:
                # Try another filename
                continue

            for row in transactions_file:
                try:
                    # TODO(Bieber): This is really unpythonic
                    row = row.decode('utf-8').replace('\n', ' ').replace('\r', ' ')
                    reader = csv.reader([row], delimiter=',', quotechar='"')
                    row = next(reader)
                    if row and len(row) > 1:
                        transaction = Transaction.create_from_row(row)
                        self.transactions.append(transaction)
                except:
                    continue


    @staticmethod
    def get_dropbox_access_token():
        flow = dropbox.client.DropboxOAuth2FlowNoRedirect(
            settings.secure.app_key,
            settings.secure.app_secret
        )

        authorize_url = flow.start()
        print('1. Go to: ' + authorize_url)
        print('2. Click "Allow" (you might have to log in first)')
        print('3. Copy the authorization code.')
        code = raw_input("Enter the authorization code here: ").strip()

        # TODO(Bieber): Persist the access_token
        access_token, user_id = flow.finish(code)
        print("access_token %s" % access_token)

        return access_token


class Transaction(object):

    # TODO(Bieber): Use enum
    # Transaction types:
    WITHDRAWAL = "WITHDRAWAL"
    TRANSFER = "TRANSFER"
    DEPOSIT = "DEPOSIT"
    BALANCE_REPORT = "BALANCE REPORT"
    EXPENSE = "EXPENSE"

    # TODO(Bieber): These should clearly be somehow distinct from the above
    SUBWAY_SWIPE = "SUBWAY SWIPE"
    LAUNDRY_CARD = "LAUNDRY CARD"

    def __init__(self,
                 transaction_type,
                 timestamp,
                 deltas,
                 balances,
                 description,
                 category=None):
        self.transaction_type = transaction_type
        self.timestamp = timestamp
        self.deltas = deltas
        self.balances = balances
        self.description = description
        self.category = category

    def __str__(self):
        if self.transaction_type == Transaction.WITHDRAWAL:
            return "%-18s WITHDRAWAL: %9.2f %-6s => %-6s %-35s" % (self.timestamp, self.deltas[1][1], self.deltas[0][0], self.deltas[1][0], self.description)
        elif self.transaction_type == Transaction.TRANSFER:
            return "%-18s TRANSFER  : %9.2f %-6s => %-6s %-35s" % (self.timestamp, self.deltas[1][1], self.deltas[0][0], self.deltas[1][0], self.description)
        elif self.transaction_type == Transaction.BALANCE_REPORT:
            return "%-18s BALANCE   : %9.2f %-16s %-35s" % (self.timestamp, self.balances[0][1], self.balances[0][0], self.description)
        elif self.transaction_type == Transaction.EXPENSE:
            return "%-18s EXPENSE   : %+9.2f %-16s %-35s" % (self.timestamp, self.deltas[0][1], self.deltas[0][0], self.description)
        return "%-18s %s" % (self.timestamp, self.description)

    def __repr__(self):
        return str(self)

    def get_resource(self):
        for resource, _ in self.deltas:
            return resource
        for resource, _ in self.balances:
            return resource

    def get_resources(self):
        resources = set()
        for resource, _ in self.deltas:
            resources.add(resource)
        for resource, _ in self.balances:
            resources.add(resource)
        return resources

    def get_net_delta(self):
        net_delta = 0
        for _, amount in self.deltas:
            net_delta += amount
        return net_delta

    def get_datetime(self):
        return timestamp_as_datetime(self.timestamp)

    def get_balances(self):
        return self.balances

    def get_deltas(self):
        return self.deltas

    @staticmethod
    def create_from_row(row):
        timestamp, transaction_str = row

        _timestamp = timestamp
        _transaction_str = transaction_str
        _deltas = []  # list of (resource, amount) pairs
        _balances = []  # list of (resource, amount) pairs
        _description = transaction_str
        _type = None

        tokens = transaction_str.lower().strip().split(' ')

        # TODO(Bieber): Replace with commands-style pattern matcher
        if Transaction.is_withdrawal(tokens):
            # withdraw {amount}
            _type = Transaction.WITHDRAWAL
            amount_str = tokens[1]
            resource_from = tokens[3]
            resource_to = tokens[5]
            amount = Transaction.amount_from_str(amount_str)

            _deltas = [
                (resource_from, -amount),
                (resource_to,   +amount),
            ]
        elif Transaction.is_transfer(tokens):
            _type = Transaction.TRANSFER
            amount_str = tokens[1]
            resource_from = tokens[3]
            resource_to = tokens[5]
            amount = Transaction.amount_from_str(amount_str)

            _deltas = [
                (resource_from, -amount),
                (resource_to,   +amount),
            ]
        elif Transaction.is_deposit(tokens):
            _type = Transaction.DEPOSIT
            raise NotImplementedError
        elif Transaction.is_balance_report(tokens):
            _type = Transaction.BALANCE_REPORT
            resource = tokens[0]
            amount_str = tokens[2]
            amount = Transaction.amount_from_str(amount_str)
            _balances = [(resource, amount)]
        elif Transaction.is_subway_swipe(tokens):
            _type = Transaction.SUBWAY_SWIPE
            # TODO(Bieber): Metrocard may be resource or may be time based
        elif Transaction.is_laundry_card_swipe(tokens):
            _type = Transaction.LAUNDRY_CARD
        elif Transaction.is_basic_expense(tokens):
            _type = Transaction.EXPENSE
            resource = tokens[0]
            amount_str = tokens[1]

            amount = Transaction.amount_from_str(amount_str)
            if not Transaction.has_sign(tokens[1]):
                amount = -amount

            _description = ' '.join(tokens[2:])
            _deltas = [(resource, amount)]

            # The change goes into the change resource instead of the cash resource
            if resource == 'cash' and amount != int(amount) and amount < 0:
                amount_spent = -amount
                change = int(amount_spent + 1) - amount_spent
                _deltas.extend([
                    ('cash', -change),
                    ('change', +change),
                ])
                _description = "{} (and ({}) in change)".format(_description, change)
        elif Transaction.is_mixed_expense(tokens):
            # TODO(Bieber): Check for mixed expense before basic expense
            # TODO(Bieber): handle mixed expense
            _type = Transaction.EXPENSE

            token_idx = 0
            while Transaction.is_amount(tokens[token_idx + 1]):
                token_idx += 2

        return Transaction(
            transaction_type=_type,
            timestamp=_timestamp,
            deltas=_deltas,
            balances=_balances,
            description=_description,
        )

    @staticmethod
    def is_withdrawal(tokens):
        return tokens[0] == 'withdraw'

    @staticmethod
    def is_transfer(tokens):
        return tokens[0] == 'transfer'

    @staticmethod
    def is_deposit(tokens):
        return tokens[0] == 'deposit'

    @staticmethod
    def is_balance_report(tokens):
        return tokens[1] == 'balance'

    @staticmethod
    def is_basic_expense(tokens):
        return len(tokens) >= 2 and Transaction.is_amount(tokens[1])

    @staticmethod
    def is_mixed_expense(tokens):
        return (len(tokens) >= 4 and
                Transaction.is_classical_resource(tokens[0]) and
                Transaction.is_amount(tokens[1]) and
                Transaction.is_classical_resource(tokens[2]) and
                Transaction.is_amount(tokens[3]))

    @staticmethod
    def is_classical_resource(resource):
        return resource.lower() in ['cash', 'change', 'credit']

    @staticmethod
    def is_subway_swipe(tokens):
        # TODO(Bieber): Ephemeral resources. Metrocards aren't forever.
        return tokens[0] == 'subway' and tokens[1] == 'swipe'

    @staticmethod
    def is_laundry_card_swipe(tokens):
        return tokens[0] == 'laundry' and tokens[1] == 'card'

    @staticmethod
    def amount_from_str(s):
        s = str(s).replace('$', '')
        return float(s)

    @staticmethod
    def is_amount(s):
        try:
            Transaction.amount_from_str(s)
            return True
        except ValueError:
            return False

    @staticmethod
    def has_sign(s):
        return s[0] == '+' or s[0] == '-'

    def counts_as_expense(self):
        if self.transaction_type != Transaction.EXPENSE:
            return False
        if "splitting" in self.description:
            return True
        return self.get_net_delta() < 0


class TransactionAccumulator(object):
    def __init__(self):
        self.deltas = defaultdict(lambda: 0)
        self.balances = defaultdict(lambda: 0)

        self.first_datetime = None
        self.last_datetime = None
        self.count = 0

    def handle_transaction(self, transaction):
        self.count += 1
        transaction_datetime = transaction.get_datetime()
        if self.first_datetime is None or transaction_datetime < self.first_datetime:
            self.first_datetime = transaction_datetime
        if self.last_datetime is None or transaction_datetime > self.last_datetime:
            self.last_datetime = transaction_datetime

        for delta in transaction.deltas:
            resource, amount = delta
            self.deltas[resource] += amount
            if resource in self.balances:
                self.balances[resource] += amount

        for balance in transaction.balances:
            resource, amount = balance
            self.balances[resource] = amount

    def get_balance(self, resources=None):
        if resources is None:
            return sum(self.balances[resource] for resource in self.balances)
        elif type(resources) is set or type(resources) is list:
            return sum(self.balances[resource] for resource in resources)
        else:
            # TODO(Bieber): Handle unseen resource more gracefully and mimic for delta
            if resources not in self.balances:
                return
            return self.balances[resources]

    def get_delta(self, resources=None):
        if resources is None:
            return sum(self.deltas[resource] for resource in self.deltas)
        elif type(resources) is set or type(resources) is list:
            return sum(self.deltas[resource] for resource in resources)
        else:
            return self.deltas[resources]

    def get_resources(self):
        resources = set()
        resources.update(r for r in self.deltas)
        resources.update(r for r in self.balances)
        return resources
