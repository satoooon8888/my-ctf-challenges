FROM tiangolo/meinheld-gunicorn-flask:latest

RUN apt update && apt install -y dc

RUN groupadd -r app && useradd -r -g app app

WORKDIR /app

COPY ./src ./
RUN chmod -R 550 .
RUN chown -R root:app .

CMD ["gunicorn", "--user", "app", "--group", "app", "--bind", "0.0.0.0:80", "main:app"]
