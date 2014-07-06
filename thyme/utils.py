from datetime import datetime

DATETIME_FORMAT = '%m/%d/%y, %H:%M %p'

def timestamp_as_datetime(timestamp):
    return datetime.strptime(timestamp, DATETIME_FORMAT)
