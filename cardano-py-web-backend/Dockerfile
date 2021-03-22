FROM node:14.16.0-alpine
LABEL maintainer="chbfiv@floydcraft.com"

USER root
WORKDIR /home/ada/app

COPY src src
COPY package.* .

RUN npm install

EXPOSE 8080
CMD ["node", "src/index.js"]



