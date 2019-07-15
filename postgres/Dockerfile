FROM postgres:11.4

# Put SQL scripts in /docker-entrypoint-initdb.d/

COPY docker-entrypoint-initdb.d/initialize_celery_database.sql /docker-entrypoint-initdb.d/initialize_celery_database.sql
