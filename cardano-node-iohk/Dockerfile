# https://docs.cardano.org/projects/cardano-node/en/latest/getting-started/install.html
# https://docs.cardano.org/projects/adrestia/en/latest/installation.html
FROM debian:buster-20210208 as stage1
LABEL maintainer="chbfiv@floydcraft.com"

ENV DEBIAN_FRONTEND=noninteractive \
    LANG=C.UTF-8 \
    ENV=/etc/profile \
    USER=root

RUN apt-get update \
    && apt-get install -y --no-install-recommends apt-utils ca-certificates sed wget curl gnupg \
    libpq-dev python3 build-essential pkg-config \
    libffi-dev libgmp-dev libssl-dev libtinfo-dev libusb-1.0-0-dev libudev-dev git \
    systemd libsystemd-dev libsodium-dev zlib1g-dev make g++ tmux git jq libncursesw5 gnupg aptitude libtool \
    autoconf secure-delete iproute2 bc tcptraceroute dialog sqlite automake sqlite3 bsdmainutils \
    && export BOOTSTRAP_HASKELL_NO_UPGRADE=1 \
    && mkdir -p /root/.cabal/bin && mkdir -p /root/.ghcup/bin \
    && curl -s -m 60 --proto '=https' --tlsv1.2 -sSf https://get-ghcup.haskell.org | sed -e 's#read.*#answer=Y;next_answer=Y;hls_answer=N#' | bash \
    && . "${HOME}"/.ghcup/env \
    && ghcup install ghc 8.10.2 \
    && ghcup set ghc 8.10.2 \
    && ghc --version \
    && ghcup install cabal

FROM stage1 as stage2
LABEL maintainer="chbfiv@floydcraft.com"

ENV APP=/opt/cardano-node \
    LANG=C.UTF-8 \
    USER=root \
    PATH=$HOME/scripts:/root/.cabal/bin:/root/.ghcup/bin:$PATH

ARG _VERSION=1.25.1

ADD stage2-files .

RUN git clone --depth 1 --branch $_VERSION https://github.com/input-output-hk/cardano-node.git \
  && export BOOTSTRAP_HASKELL_NO_UPGRADE=1 \
  && cd cardano-node \
  && echo "package cardano-crypto-praos" > cabal.project.local \
  && echo "   flags: -external-libsodium-vrf" >> cabal.project.local \
  && chmod +x /scripts/cabal-build-all.sh \
  && bash /scripts/cabal-build-all.sh \
  && cardano-node --version

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

COPY --from=stage2 /root/.cabal/bin/* /usr/local/bin/
COPY --from=stage2 /lib/x86_64-linux-gnu/lib* /lib/x86_64-linux-gnu/
COPY --from=stage2 /lib64/ld-linux-x86-64* /lib64/
COPY --from=stage2 /usr/lib/x86_64-linux-gnu/libgmp.* /usr/lib/x86_64-linux-gnu/
COPY --from=stage2 /usr/lib/x86_64-linux-gnu/liblz4.* /usr/lib/x86_64-linux-gnu/
COPY --from=stage2 /usr/lib/x86_64-linux-gnu/libsodium.* /usr/lib/x86_64-linux-gnu/
COPY --from=stage2 /opt/ /opt/

ADD stage3-files .

RUN apt-get update \
    && apt-get install --no-install-recommends -y ca-certificates libcap2-bin ncurses-bin iproute2 curl wget xz-utils netbase sudo coreutils dnsutils net-tools procps tcptraceroute bc \
    && apt-get -y clean \
    && apt-get -y autoremove \
    && rm -rf /var/lib/apt/lists/* \
    && chmod +x scripts/entrypoint.sh \
    && mkdir -p /storage/mainnet /storage/testnet

EXPOSE 3001 12798 12788
ENTRYPOINT [ "scripts/entrypoint.sh" ]