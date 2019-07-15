# Use an official Python runtime as a parent image
FROM python:3.6-alpine

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install --trusted-host pypi.python.org celery
RUN pip install --trusted-host pypi.python.org sqlalchemy
RUN pip install --trusted-host pypi.python.org psycopg2

# Set the working directory to /opt
WORKDIR /opt/celery-beat

# Copy the current directory contents into the container at /opt
ADD . /opt/celery-beat

CMD ["celery", "beat",  "-A",  "app"]