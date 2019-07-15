from celery import Celery

app = Celery('tasks', broker='pyamqp://guest:guest@10.0.75.1//', backend='db+postgresql://postgres:postgres@10.0.75.1/celery')

app.conf.beat_schedule = {
    'add-every-5-seconds': {
        'task': 'tasks.add',
        'schedule': 5.0,
        'args': (16, 16)
    },
}
app.conf.timezone = 'UTC'