from __future__ import absolute_import

import os
import django


from celery import Celery
from django.conf import settings

import datetime
import celery



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.settings')

django.setup()

app = Celery('src')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


app.conf.update(
	BROKER_URL = 'redis://127.0.0.1:6379/0',
	BROKER_TRANSPORT = 'redis',
	CELERYBEAT_SCHEDULE = {
	    'greet-every-3-seconds': {
	        'task': 'hello_world',
	        'schedule': datetime.timedelta(minutes=1)
	    },
	}
)
