from __future__ import absolute_import

from apscheduler.executors.pool import ProcessPoolExecutor
from apscheduler.executors.pool import ThreadPoolExecutor
from apscheduler.jobstores.redis import RedisJobStore
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.date import DateTrigger

from datetime import datetime
from datetime import timedelta
import parsedatetime

from subprocess import Popen
from time import sleep

import daemon
import daemon.pidfile
import json
import redis

from sendlater.mailer import Mailer
from settings import settings

mailer = Mailer()
mailer.login(settings.secure.GMAIL_USER, settings.secure.GMAIL_PASSWD)

def send_message(recipient, sender, when, message):
    # Temporary email address mapping
    if recipient.lower() in ['biebs', 'david', 'bieber', 'david bieber']:
        recipient = 'david810+sendlater@gmail.com'
    elif recipient.lower() == 'olshansky':
        recipient = 'olshanskydaniel+sendlater@gmail.com'

    # Determine the message subject
    tokens = message[:60].split(' ')
    try:
        if message[60] == ' ':
            tokens = tokens[:-1]
    except:
        pass
    subject = ' '.join(tokens)

    mailer.unix_mail(
        user='alerts',
        to=recipient,
        subject=subject,
        text=message,
    )

def main():
    context = daemon.DaemonContext(
        working_directory='/opt/sendlater',
        pidfile=daemon.pidfile.PIDLockFile('/var/run/sendlater.pid'),
    )

    with context:
        executors = {
            'default': ThreadPoolExecutor(20),
            'processpool': ProcessPoolExecutor(5),
        }

        scheduler = BackgroundScheduler(executors=executors)
        scheduler.add_jobstore(
            'redis',
            jobs_key='sendlater:jobs',
            run_times_key='sendlater:run_times',
        )
        scheduler.start()

        datetime_parser = parsedatetime.Calendar()
        def process(text):
            data = json.loads(text)

            recipient = data.get('recipient')
            sender = data.get('sender')
            when = data.get('when')
            message = data.get('message')

            parsed_tuples = datetime_parser.nlp(when)
            parsed_tuple = parsed_tuples[0]
            dt, flags, start_pos, end_pos, matched_text = parsed_tuple

            trigger = DateTrigger(dt)
            scheduler.add_job(
                send_message,
                trigger=trigger,
                args=[recipient, sender, when, message],
            )

        r = redis.Redis()

        while True:
            queue_name, text = r.blpop('sendlater:messages')
            try:
                process(text)
            except:
                pass

if __name__ == '__main__':
    main()
