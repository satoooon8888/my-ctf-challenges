FROM node:lts-slim

ENV NODE_ENV=production

RUN apt-get update \
    && apt-get install -y wget gnupg \
	&& wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list\
    && apt-get update && apt-get -y install google-chrome-stable

WORKDIR /app

COPY src/package.json src/package-lock.json ./

RUN npm install . --omit-dev

COPY src/ .

CMD ["node", "server.js"]

