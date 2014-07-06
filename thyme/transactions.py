import csv
import dropbox
from utils import timestamp_as_datetime

try:
    import secure_settings as settings
except:
    import secure_settings_template as settings


class TransactionLoader(object):

    def __init__(self, use_dropbox=True):

        if use_dropbox:
            self.dropbox_client = dropbox.client.DropboxClient(settings.access_token)

            # TODO(Bieber): Cache the file
            transactions_file, metadata = self.dropbox_client.get_file_and_metadata('/Transactions.csv')
        else:
            transactions_file = open('Transactions.csv')

        reader = csv.reader(transactions_file, delimiter=',', quotechar='"')
        self.transactions = []
        for row in reader:
            transaction = Transaction.create_from_row(row)
            self.transactions.append(transaction)

    @staticmethod
    def get_dropbox_access_token():
        flow = dropbox.client.DropboxOAuth2FlowNoRedirect(
            settings.app_key,
            settings.app_secret
        )

        authorize_url = flow.start()
        print '1. Go to: ' + authorize_url
        print '2. Click "Allow" (you might have to log in first)'
        print '3. Copy the authorization code.'
        code = raw_input("Enter the authorization code here: ").strip()

        # TODO(Bieber): Persist the access_token
        access_token, user_id = flow.finish(code)
        print "access_token", access_token

        return access_token


class Transaction(object):

    # TODO(Bieber): Use enum
    # Transaction types:
    WITHDRAWL = "WITHDRAWL"
    DEPOSIT = "DEPOSIT"
    BALANCE_REPORT = "BALANCE REPORT"
    EXPENSE = "EXPENSE"

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
        return "%s" % (self.transaction_type)

    def __repr__(self):
        return str(self)

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

        if Transaction.is_withdrawl(tokens):
            _type = Transaction.WITHDRAWL
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
        elif Transaction.is_expense(tokens):
            _type = Transaction.EXPENSE
            resource = tokens[0]
            amount_str = tokens[1]

            amount = Transaction.amount_from_str(amount_str)
            if not Transaction.has_sign(tokens[1]):
                amount *= -1

            _description = ' '.join(tokens[2:])
            _deltas = [(resource, amount)]

        return Transaction(
            transaction_type=_type,
            timestamp=_timestamp,
            deltas=_deltas,
            balances=_balances,
            description=_description,
        )

    @staticmethod
    def is_withdrawl(tokens):
        return tokens[0] == 'withdraw'

    @staticmethod
    def is_deposit(tokens):
        return tokens[0] == 'deposit'

    @staticmethod
    def is_balance_report(tokens):
        return tokens[1] == 'balance'

    @staticmethod
    def is_expense(tokens):
        return len(tokens) >= 2

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

