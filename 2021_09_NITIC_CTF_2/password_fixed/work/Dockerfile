FROM tiangolo/uwsgi-nginx-flask:python3.8-alpine

RUN apk update
RUN adduser -D web
RUN pip install Flask

WORKDIR /home/web

COPY ./server.py ./
COPY ./templates/index.html ./templates/
COPY ./flag.txt ./
COPY ./uwsgi.ini ./

RUN chown root:web -R ./
