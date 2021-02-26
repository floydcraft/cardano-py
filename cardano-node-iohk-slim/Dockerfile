ARG _VERSION=1.25.1
FROM debian:buster-20210208-slim
LABEL maintainer="chbfiv@floydcraft.com"

ARG DEBIAN_FRONTEND=noninteractive

ENV ENV=/etc/profile \
    LC_ALL=en_US.UTF-8 \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US.UTF-8 \
    NODE_HOME=/opt/cardano-node \
    PATH=/opt/cardano-node/scripts:/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin

USER root
WORKDIR /

COPY --from=floydcraft/cardano-node-iohk:latest /root/.cabal/bin/* /usr/local/bin/
COPY --from=floydcraft/cardano-node-iohk:latest /lib/x86_64-linux-gnu/lib* /lib/x86_64-linux-gnu/
COPY --from=floydcraft/cardano-node-iohk:latest /lib64/ld-linux-x86-64* /lib64/
COPY --from=floydcraft/cardano-node-iohk:latest /usr/lib/x86_64-linux-gnu/libgmp.* /usr/lib/x86_64-linux-gnu/
COPY --from=floydcraft/cardano-node-iohk:latest /usr/lib/x86_64-linux-gnu/liblz4.* /usr/lib/x86_64-linux-gnu/
COPY --from=floydcraft/cardano-node-iohk:latest /usr/lib/x86_64-linux-gnu/libsodium.* /usr/lib/x86_64-linux-gnu/
COPY --from=floydcraft/cardano-node-iohk:latest /opt/ /opt/
COPY --from=floydcraft/cardano-node-iohk:latest /scripts/entrypoint.sh /scripts/entrypoint.sh
COPY --from=floydcraft/cardano-node-iohk:latest /config/ /config/

RUN apt-get update \
    && apt-get install --no-install-recommends -y ca-certificates libcap2-bin ncurses-bin iproute2 curl wget xz-utils netbase sudo coreutils dnsutils net-tools procps tcptraceroute bc \
    && apt-get -y clean \
    && apt-get -y autoremove \
    && rm -rf /var/lib/apt/lists/* \
    && chmod +x scripts/entrypoint.sh

EXPOSE 3001 12798 12788
ENTRYPOINT [ "scripts/entrypoint.sh" ]