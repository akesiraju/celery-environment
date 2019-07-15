from celery import Celery
import time

app = Celery('tasks', broker='pyamqp://guest:guest@10.0.75.1//', backend='db+postgresql://postgres:postgres@10.0.75.1/celery')

@app.task (max_retries=5, time_limit=15)
def add(x, y):    
    return x + y    