FROM continuumio/miniconda3:latest

WORKDIR /app
ADD . ./

RUN conda update conda
RUN conda env update --name root -f environment.yml

CMD gunicorn -b :8080 redhill.wsgi