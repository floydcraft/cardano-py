FROM alpine:3.13.1

# removed:  libsystemd-dev, libtinfo-dev
# extras from the guild: v libpq-dev python3 systemd libsodium-dev libncursesw5 gnupg aptitude libtool autoconf secure-delete iproute2 bc tcptraceroute dialog sqlite automake sqlite3 bsdmainutils libusb-1.0-0-dev libudev-de
RUN apk add --no-cache sed curl wget gnupg git pkgconfig libffi-dev gmp-dev openssl-dev  zlib-dev make g++ tmux git jq wget ncurses-dev \
    && unset BOOTSTRAP_HASKELL_NONINTERACTIVE \
    && export BOOTSTRAP_HASKELL_NO_UPGRADE=1 \
    && curl -s -m 60 --proto '=https' --tlsv1.2 -sSf https://get-ghcup.haskell.org | sed -e 's#read.*#answer=Y;next_answer=Y;hls_answer=N#' | sh \
    && . "${HOME}"/.ghcup/env \
    && ghcup install ghc 8.10.2 \
    && ghcup set ghc 8.10.2 \
    && ghc --version \
    && ghcup install cabal

ENTRYPOINT [ ]