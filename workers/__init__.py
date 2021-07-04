from celery import Celery

app = Celery('celery name')

app.config_from_object('workers.celeryconfig')

# app.autodiscover_tasks(['workers.tasks'])