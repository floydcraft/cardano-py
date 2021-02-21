# https://docs.cardano.org/projects/cardano-node/en/latest/getting-started/install.html
# https://docs.cardano.org/projects/adrestia/en/latest/installation.html
FROM floydcraft/haskell:latest
LABEL maintainer="chbfiv@floydcraft.com"

ENV APP=/opt/cardano-node \
    LANG=C.UTF-8 \
    USER=root \
    PATH=$HOME/scripts:/root/.cabal/bin:/root/.ghcup/bin:$PATH

ARG _VERSION=1.25.1

ADD files .

RUN git clone --depth 1 --branch $_VERSION https://github.com/input-output-hk/cardano-node.git \
  && export BOOTSTRAP_HASKELL_NO_UPGRADE=1 \
  && cd cardano-node \
  && echo "package cardano-crypto-praos" > cabal.project.local \
  && echo "   flags: -external-libsodium-vrf" >> cabal.project.local \
  && bash /scripts/cabal-build-all.sh \
  && cardano-node --version \
  && chmod +x /scripts/entrypoint.sh

EXPOSE 3001 12798 12788
ENTRYPOINT [ "scripts/entrypoint.sh" ]