FROM debian:buster-20210208 as stage1
LABEL maintainer="chbfiv@floydcraft.com"

ARG _VERSION=8.10.2

ENV DEBIAN_FRONTEND=noninteractive \
    LANG=C.UTF-8 \
    ENV=/etc/profile \
    USER=root

ADD files .

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
    && ghcup install ghc $_VERSION \
    && ghcup set ghc $_VERSION \
    && ghc --version \
    && ghcup install cabal \
    && chmod +x /scripts/cabal-build-all.sh

ENTRYPOINT []