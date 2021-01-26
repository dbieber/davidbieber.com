import os

import dateparser


def publish():
  uid = os.environ.get('SNIPPET_UID')
  title = os.environ.get('SNIPPET_TITLE')
  content = os.environ.get('SNIPPET_CONTENT')
  date = os.environ.get('SNIPPET_DATE')
  date = dateparser.parse(date)
  date_str = date.strftime('%Y-%m-%dT%H:%M:00')

  print(uid, title, content, date_str)

  filename_title = (
      title.lower()
      .replace(' ', '-')
      .replace(",", '')
      .replace(".", '')
      .replace("/", '')
      .replace("^", '')
      .replace("#", '')
      .replace("@", '')
      .replace("&", '')
      .replace("*", '')
      .replace("%", '')
      .replace("?", '')
      .replace(":", '')
      .replace("!", '')
      .replace("'", '')
      .replace('"', '')
      .replace('(', '')
      .replace(')', '')
      .replace('“', '')
      .replace('”', '')
  )

  # Determine filepath.
  content_path = 'davidbieber.com-main/hugo/content'
  if uid == 'now-page':
    filepath = os.path.join(content_path, 'now.md')
  else:
    filename_date = date.strftime('%Y-%m-%d')
    filename = f'{filename_date}-{filename_title}.md'
    snippets_dir = os.path.join(content_path, 'snippets')
    filepath = os.path.join(snippets_dir, filename)

  content = content.replace('```\n', '\n```\n')
  content = content.replace('$$', '$')
  content = content.replace(r'\{', '{')
  content = content.replace(r'\}', '}')
  content = content.replace(r'\[', '[')
  content = content.replace(r'\]', ']')
  content = content.replace('\\\\', '\\\\\\\\\\\\')

  # Determine frontmatter.
  frontmatter = None
  additional_frontmatter = ''
  if frontmatter is not None:
    additional_frontmatter = frontmatter
  else:
    if '\\frac' in content or '\\infty' in content:
      additional_frontmatter = 'math = true'
    elif '[^1]' in content:
      additional_frontmatter = 'plugins_js = ["margin-notes"]'

  # Determine content.
  if uid == 'now-page':
    content = f"""
_Last updated on {date.strftime('%Y-%m-%d')}._

{content}
    """

  content = f"""+++
title = "{title}"
date = {date_str}
uid = "{uid}"
{additional_frontmatter}
+++

{content}
"""

  with open(filepath, 'w') as f:
    f.write(content)


if __name__ == '__main__':
  publish()
