# https://github.com/input-output-hk/cardano-db-sync/blob/master/doc/building-running.md
FROM floydcraft/cardano-node-config:latest
LABEL maintainer="chbfiv@floydcraft.com"

ENV APP=/opt/cardano-db-node \
    LANG=C.UTF-8 \
    USER=root \
    PATH=$HOME/scripts:/root/.cabal/bin:/root/.ghcup/bin:$PATH

ARG _VERSION=8.0.0

ADD files/ .

RUN git clone --depth 1 --branch $_VERSION https://github.com/input-output-hk/cardano-db-sync.git \
  && export BOOTSTRAP_HASKELL_NO_UPGRADE=1 \
  && cd cardano-db-sync \
  && echo "package cardano-crypto-praos" > cabal.project.local \
  && echo "   flags: -external-libsodium-vrf" >> cabal.project.local \
  && bash /scripts/cabal-build-all.sh \
  && cardano-db-sync --version \
  && apt-get update \
  && apt-get install -y sudo libpq-dev libpq5 postgresql \
  && mkdir /schema \
  && cp schema/* /schema \
  && cp scripts/* /scripts

EXPOSE 3001 12798 12788 5432
ENTRYPOINT [ "scripts/entrypoint.sh" ]