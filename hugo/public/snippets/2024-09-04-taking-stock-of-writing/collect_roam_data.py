import roam
import pandas as pd
import matplotlib.pyplot as plt
from collections import defaultdict


def count_words(text):
    return len(str(text).split())


def get_timestamp(item):
    # Try to get 'create-time', fall back to 'edit-time' if not available
    return item.get('create-time') or item.get('edit-time')


def process_data(data):
    word_counts = defaultdict(int)
    for item in data.values():
        timestamp = get_timestamp(item)
        if timestamp is None:
            continue  # Skip items without any timestamp
        
        date = pd.to_datetime(timestamp, unit='ms')
        if 2019 <= date.year <= 2024:
            words = count_words(item.get('title', ''))
            if 'string' in item:
                words += count_words(item['string'])
            word_counts[(date.year, date.month)] += words
    return word_counts

def plot_activity(word_counts):
    df = pd.DataFrame(list(word_counts.items()), columns=['date', 'word_count'])
    df['date'] = pd.to_datetime(df['date'].apply(lambda x: f"{x[0]}-{x[1]:02d}-01"))
    df = df.set_index('date').sort_index()
    
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['word_count'])
    plt.title('Writing Activity by Month (2019-2024)')
    plt.xlabel('Date')
    plt.ylabel('Word Count')
    plt.grid(True)
    plt.tight_layout()
    plt.show()


all_indexed_by_uid = roam.get_all_indexed_by_uid()
word_counts = process_data(all_indexed_by_uid)
plot_activity(word_counts)
