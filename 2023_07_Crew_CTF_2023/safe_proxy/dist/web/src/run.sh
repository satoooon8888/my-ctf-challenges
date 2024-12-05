#!/bin/sh

deno run --no-prompt --allow-net=0.0.0.0:8080,flag-provider:8080 --allow-read=. --allow-env ./main.js
