FROM node:12.14.0 as base

WORKDIR /home/ada/frontend

COPY frontend .

RUN npm install -g @angular/cli \
    && npm install \
    && ng build --prod

FROM node:14.16.0-alpine
LABEL maintainer="chbfiv@floydcraft.com"

USER root
WORKDIR /home/ada/frontend

COPY --from=base /home/ada/frontend/public public

WORKDIR /home/ada/backend
COPY backend .

RUN npm install --only=production

EXPOSE 8080
CMD ["node", "src/index.js"]



