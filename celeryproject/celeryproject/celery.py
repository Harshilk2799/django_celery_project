import os
from time import sleep
from datetime import timedelta
from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celeryproject.settings')

app = Celery('celeryproject')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

# Method 2
# app.conf.beat_schedule = {
#     "every-10-seconds": {
#         "task": "App.tasks.clear_session_cache",
#         "schedule":10,
#         "args":("1111",)
#     },
#     # Add more periodic tasks as needed
# }


# Using timedelta
# app.conf.beat_schedule = {
#     "every-10-seconds": {
#         "task": "App.tasks.clear_session_cache",
#         "schedule":timedelta(seconds=10),
#         "args":("1111",)
#     },
#     # Add more periodic tasks as needed
# }


# Using crontab
# app.conf.beat_schedule = {
#     "every-10-seconds": {
#         "task": "App.tasks.clear_session_cache",
#         "schedule":crontab(minute="*/1"),
#         "args":("1111",)
#     },
#     # Add more periodic tasks as needed
# }

# Create a Task
@app.task(name="Addition_task")
def add(x, y):
    sleep(20)
    return x + y