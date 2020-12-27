import os

import dateparser


def publish():
  uid = os.environ.get('SNIPPETS_UID')
  title = os.environ.get('SNIPPETS_TITLE')
  content = os.environ.get('SNIPPETS_CONTENT')
  date = os.environ.get('SNIPPETS_DATE')
  date = dateparser.parse(date)
  date_str = date.strftime('%Y-%m-%dT%H:%M:00')

  print(uid, title, content, date_str)

  frontmatter = None
  additional_frontmatter = ''
  if frontmatter is not None:
    additional_frontmatter = frontmatter
  else:
    if '\\frac' in content:
      additional_frontmatter = 'math = true'

  content = f"""+++
title = "{title}"
date = {date_str}
uid = "{uid}"
{additional_frontmatter}
+++

{content}
"""
  filename_title = (
      title.lower()
      .replace(' ', '-')
      .replace("/", '')
      .replace("'", '')
      .replace('"', '')
      .replace('(', '')
      .replace(')', '')
      .replace('“', '')
      .replace('”', '')
  )

  filename_date = date.strftime('%Y-%m-%d')
  filename = f'{filename_date}-{filename_title}.md'
  snippets_dir = 'davidbieber.com-main/hugo/content/snippets'
  filepath = os.path.join(snippets_dir, filename)
  with open(filepath, 'w') as f:
    f.write(content)


if __name__ == '__main__':
  publish()
