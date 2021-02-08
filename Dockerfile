# https://docs.cardano.org/projects/adrestia/en/latest/installation.html
FROM inputoutput/cardano-node:1.25.1
LABEL maintainer="chbfiv@floydcraft.com"

ENV CARDANO_NETWORK mainnet
#ARG DEBIAN_FRONTEND=noninteractive
#USER root
#WORKDIR /

ADD files .

EXPOSE 3001
RUN chmod +x entrypoint.sh
ENTRYPOINT [ "./entrypoint.sh" ]