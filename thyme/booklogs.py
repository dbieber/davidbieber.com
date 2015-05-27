from __future__ import absolute_import

from collections import defaultdict
import re

import csv
import dropbox

from settings import settings
from thyme.utils import timestamp_as_datetime


class BookLogLoader(object):

    def __init__(self, use_dropbox=True, filenames=None):

        self.logs = []

        possible_filenames = filenames or [
            '/Reading 2015.csv',
            '/Reading.csv',
        ]

        for filename in possible_filenames:
            try:
                if use_dropbox:
                    self.dropbox_client = dropbox.client.DropboxClient(settings.secure.access_token)

                    # TODO(Bieber): Cache the file
                    logs_file, metadata = self.dropbox_client.get_file_and_metadata(filename)
                else:
                    logs_file = open(filename ,'r')

                for row in logs_file:
                    try:
                        # TODO(Bieber): This is really unpythonic
                        row = row.decode('utf-8')
                        reader = csv.reader([row], delimiter=',', quotechar='"')
                        row = next(reader)
                        if row and len(row) > 1:
                            log = BookLog.create_from_row(row)
                            self.logs.append(log)
                    except:
                        continue
            except:
                pass

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

class BookLog(object):

    # TODO(Bieber): Use enum
    # Log types:
    DEFAULT = "DEFAULT"

    def __init__(self,
                 log_type,
                 timestamp,
                 title,
                 author=None,
                 note=None,
                 category=None,
                 progress=None):
        self.log_type = log_type
        self.timestamp = timestamp
        self.title = title
        self.author = author
        self.note = note
        self.category = category
        self.progress = progress

    def __str__(self):
        title = self.title or ""
        author = self.author or ""
        note = self.note or ""
        return "{} by {}: {}".format(title, author, note)

    def __repr__(self):
        return str(self)

    def get_datetime(self):
        return timestamp_as_datetime(self.timestamp)

    @staticmethod
    def is_page_range(s):
        try:
            return BookLog.as_page_range(s) is not None
        except ValueError:
            return False

    @staticmethod
    def as_page_range(s):
        patterns = ['{} - {}', '{}', 'ch{}']
        for pattern in patterns:
            regex_str = pattern.replace('{}', '(\d+)')
            regex_str = regex_str.replace(' ', '\s*')
            regex = re.compile(regex_str)
            match = regex.match(s)
            if match:
                return match.groups()
        raise ValueError

    def get_information(self):
        patterns = {
            UPDATE_1: "{title} by {author} {page_range} {note}?",
            UPDATE_2: "{title} {page_range} {note}?",
            NEW_BOOK: "started {title}",
        }

        for pattern_type in patterns:
            pattern = patterns[pattern_type]
            pattern = pattern.replace('{title}', '(.*)')
            pattern = pattern.replace('{page_range}', page_range_regex_str)
            pattern = pattern.replace('{page_range}', page_range_regex_str)

    @staticmethod
    def create_from_row(row):
        timestamp, log_str = row

        _log_str = log_str
        _log_type = BookLog.DEFAULT
        _timestamp = timestamp
        _title = None
        _author = None
        _note = None
        _category = None
        _progress = None

        tokens = log_str.lower().strip().split(' ')

        # Temporary code until pattern matching engine is in place:
        page_range_index = None
        page_range_end_index = None
        for i, token in enumerate(tokens):
            if token[0] == '(':
                for j, end_token in enumerate(tokens[i:]):
                    if end_token[-1] == ')':
                        break
                page_range_index = i
                page_range_end_index = i + j
                _progress = ' '.join(tokens[i:i+j+1])
                break

            if BookLog.is_page_range(token):
                page_range_index = i
                page_range_end_index = i
                _progress = token
                break

        if 'by' in tokens:
            by_index = tokens.index('by')
            _title = ' '.join(tokens[:by_index])
            _author = ' '.join(tokens[by_index+1:page_range_index])
        elif page_range_index:
            _title = ' '.join(tokens[:page_range_index])

        if page_range_end_index is not None:
            possible_note = ' '.join(tokens[page_range_end_index+1:])
            if len(possible_note):
                _note = possible_note

        return BookLog(
            log_type=_log_type,
            timestamp=_timestamp,
            title=_title,
            author=_author,
            note=_note,
            category=_category,
            progress=_progress,
        )

class BookRecord(object):
    def __init__(self):
        self.author = None
        self.title = None
        self.progress = []  # sorted list of page ranges read
        self.notes = []  # list of (timestamp, string) tuples
        self.last_updated = None

    @staticmethod
    def create_from_log(log):
        record = BookRecord()
        record.process_log(log)
        return record

    def process_log(self, log):
        self.author = self.author or log.author
        self.title = self.title or log.title
        self.last_updated = log.timestamp
        self.add_progress(log.progress)
        if log.note:
            self.notes.append((log.timestamp, log.note))

    def add_progress(self, progress):
        # TODO(Bieber): Add interesting intersection and binary search logic.
        if progress is not None:
            self.progress.append(progress)

class BookLogAccumulator(object):
    def __init__(self):
        self.first_datetime = None
        self.last_datetime = None
        self.dates_read = set()
        self.current_book_id = None

        self.book_records = {}

    def get_book_id(self, log):
        if log.title is None:
            return self.current_book_id
        else:
            return log.title

    def handle_log(self, log, modify_logs=True):
        log_datetime = log.get_datetime()
        self.dates_read.add(log_datetime.date())
        if self.first_datetime is None or log_datetime < self.first_datetime:
            self.first_datetime = log_datetime
        if self.last_datetime is None or log_datetime > self.last_datetime:
            self.last_datetime = log_datetime

        book_id = self.get_book_id(log)

        # TODO(Bieber): Fill in gaps in the log using book_records as well
        # as the internet. Later: cache the data we look up.

        if book_id not in self.book_records:
            current_book_record = BookRecord.create_from_log(log)
        else:
            current_book_record = self.book_records[book_id]
            current_book_record.process_log(log)

        self.book_records[book_id] = current_book_record

        if modify_logs:
            log.title = current_book_record.title
            log.author = current_book_record.author

        self.current_book_id = book_id
