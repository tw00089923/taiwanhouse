
# base image
FROM postgres:10.4-alpine
# run create.sql on init
ENV POSTGRES_USER psql
ENV POSTGRES_PASSWORD 12345
ADD create.sql /docker-entrypoint-initdb.d