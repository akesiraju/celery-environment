FROM python:3.6-alpine

RUN pip install --trusted-host pypi.python.org celery
RUN pip install --trusted-host pypi.python.org flower

EXPOSE 5555

CMD ["celery", "flower", "--port=5555", "--broker=amqp://guest:guest@10.0.75.1:5672//"]