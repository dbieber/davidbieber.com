from collections import defaultdict
from datetime import datetime
import re
from bs4 import BeautifulSoup

import snippets


def clean_html(raw_html):
    # Remove HTML tags
    cleantext = BeautifulSoup(raw_html, "html.parser").text
    # Remove special characters and digits
    cleantext = re.sub(r'[^a-zA-Z\s]', '', cleantext)
    return cleantext


def count_words(text):
    return len(text.split())


def calculate_word_counts(snippets):
    word_counts = defaultdict(int)
    
    for snippet in snippets:
        # Parse the publication date
        pub_date = datetime.strptime(snippet.pubDate, '%a, %d %b %Y %H:%M:%S %z')
        
        # Clean the text and count words
        clean_title = clean_html(snippet.title)
        clean_description = clean_html(snippet.description)
        total_words = count_words(clean_title) + count_words(clean_description)
        
        # Add to the word count for this month
        month_key = (pub_date.year, pub_date.month)
        word_counts[month_key] += total_words
    
    return word_counts


# Get the snippet data
snippets_from_website = snippets.getSnippetsFromWebsite()

# Calculate word counts
monthly_word_counts = calculate_word_counts(snippets_from_website)

# Print results
for (year, month), count in sorted(monthly_word_counts.items()):
    print(f"{year}-{month:02d}: {count} words")

# Optionally, return the data in a format suitable for your JavaScript chart
chart_data = [
    {"month": f"{year}-{month:02d}", "wordCount": count}
    for (year, month), count in sorted(monthly_word_counts.items())
]

print("\nChart data:")
print(chart_data)


