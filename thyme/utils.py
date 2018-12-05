from datetime import datetime
from datetime import timedelta


DATETIME_FORMAT = '%m/%d/%y, %H:%M %p'

def timestamp_as_datetime(timestamp):
    dt = datetime.strptime(timestamp, DATETIME_FORMAT)
    if "PM" in timestamp and dt.hour != 12:
        dt += timedelta(hours=12)
    elif "AM" in timestamp and dt.hour == 12:
        dt -= timedelta(hours=12)
    return dt

def category_as_link(category):
    return '<a href="/thyme/expenses_by_category/{category_lower}">{category}</a>'.format(
        category_lower=category.lower().strip(),
        category=category,
    )
