FROM python:3.8.7-alpine3.11

ARG PORT=9000

RUN apk update
RUN apk add gcc musl-dev

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install pycryptodome pycryptodomex

ADD ./server.py /app/server.py
ADD ./primes.txt /app/primes.txt
ADD ./flag.txt /app/flag.txt

RUN apk add socat

RUN echo socat TCP-L:${PORT},reuseaddr,fork EXEC:/app/server.py,stderr > /app/entry.sh

WORKDIR /app
ENTRYPOINT /bin/sh /app/entry.sh

# TODO: 動作確認

