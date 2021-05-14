FROM node:12.14.0 as base

WORKDIR /home/ada
COPY frontend frontend
COPY backend backend

RUN cd /home/ada/frontend \
    && npm install -g @angular/cli \
    && npm install \
    && ng build --prod \
    && cd /home/ada/backend \
    && npm install \
    && npm build --prod

FROM node:14.16.0-alpine
LABEL maintainer="chbfiv@floydcraft.com"

USER root
WORKDIR /home/ada

COPY --from=base /home/ada/frontend/dist frontend/
COPY --from=base /home/ada/backend backend/
COPY --from=base /home/ada/backend/package.json /home/ada/backend/package-lock.json backend/

WORKDIR /home/ada/backend
COPY backend .

RUN npm install --only=production

EXPOSE 8080
CMD ["node", "src/index.js"]



