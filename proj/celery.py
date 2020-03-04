from __future__ import absolute_import, unicode_literals
from django.conf import settings

import os

from celery import Celery
from celery.schedules import crontab
from time import sleep

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')

app = Celery('proj')

app.conf.timezone = 'UTC'

redis='redis://localhost:6379'
app.conf.broker_url = redis
#app.conf.broker_url = 'sqs://AKIARJLDNDHBUNFR7PVK:lWpWXK91cRaKkFJwoCzO6tE24XhfdQEsfT8Gzj57@'


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    delay= 3

    sender.add_periodic_task(delay, test.s(delay), name='add every 2 second')


@app.task
def test(delay):
    print("task every " + str(delay) +  " seconds")