FROM python:3.9-slim
LABEL maintainer="chbfiv@floydcraft.com"

ARG DEBIAN_FRONTEND=noninteractive

RUN python -m pip install setuptools wheel twine yolk3k bump2version

ENTRYPOINT [ "python" ]