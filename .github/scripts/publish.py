import os

def publish():
  uid = os.environ.get('SNIPPETS_UID')
  title = os.environ.get('SNIPPETS_TITLE')
  content = os.environ.get('SNIPPETS_CONTENT')
  date = os.environ.get('SNIPPETS_DATE')
  print(uid, title, content, date)
