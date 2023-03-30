import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

app = Celery('app')
app.conf.broker_url = 'redis://redis:6379/0'
app.autodiscover_tasks()