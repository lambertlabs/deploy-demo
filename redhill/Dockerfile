FROM continuumio/miniconda3:latest

WORKDIR /app
ADD . ./

RUN conda update conda
RUN conda env update --name root -f environment.yml

ENV RED_DATABASE_NAME='AAA' \
RED_DATABASE_USER='AAA' \
RED_DATABASE_PASS='AAA' \
RED_DJANGO_SECRET='AAA'

CMD gunicorn -b :8080 redhill.wsgi