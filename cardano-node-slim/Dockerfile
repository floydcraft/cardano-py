ARG _VERSION=1.25.1
FROM floydcraft/cardano-node-iohk-slim:latest
LABEL maintainer="chbfiv@floydcraft.com"

ADD files/ .

RUN cd cardanopy && python setup.py install && cd .. && rm -rf cardanopy