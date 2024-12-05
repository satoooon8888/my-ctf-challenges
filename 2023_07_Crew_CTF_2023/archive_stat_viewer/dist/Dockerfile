FROM tiangolo/meinheld-gunicorn-flask:latest

RUN pip install flask

RUN groupadd -r app && useradd -r -g app app

WORKDIR /app

COPY ./src ./
RUN chmod -R 550 .
RUN chown -R root:app .
RUN mkdir archives && chmod a+w archives


CMD ["gunicorn", "--user", "app", "--group", "app", "--bind", "0.0.0.0:80", "main:app"]
