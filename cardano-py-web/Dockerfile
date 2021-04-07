FROM node:12.14.0 as base

WORKDIR /home/ada/app

COPY frontend .

RUN npm install -g @angular/cli \
    && npm install \
    && ng build --prod

FROM node:14.16.0-alpine
LABEL maintainer="chbfiv@floydcraft.com"

USER root
WORKDIR /home/ada/app

COPY --from=base /home/ada/app/dist/cardano-py-web dist/cardano-py-web
COPY backend .

RUN npm install --only=production

EXPOSE 8080
CMD ["node", "src/index.js"]



