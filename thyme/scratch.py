from transactions import TransactionLoader

loader = TransactionLoader(use_dropbox=False)
for transaction in loader.transactions:
    print transaction
