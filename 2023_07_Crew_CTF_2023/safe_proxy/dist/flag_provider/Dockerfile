ARG DENO_VERSION=1.32.3

FROM denoland/deno:bin-$DENO_VERSION AS deno
FROM ubuntu
COPY --from=deno /deno /usr/local/bin/deno

EXPOSE 8080

RUN useradd app

USER app

WORKDIR /home/app

COPY ./src .

CMD ["./run.sh"]
