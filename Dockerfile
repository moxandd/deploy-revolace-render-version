FROM python:3.12-slim

COPY . /main/
WORKDIR /main

RUN apt-get update && \
    apt-get install -y \
    build-essential \
    python3-dev \
    python3-setuptools \
    libpq-dev \
    gcc \
    make

RUN python3 -m venv /opt/venv && \
    /opt/venv/bin/python -m pip install pip --upgrade && \
    /opt/venv/bin/python -m pip install -r /main/requirements.txt

RUN apt-get remove -y --purge make gcc build-essential \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

RUN chmod +x ./deploy_config/entrypoint.sh

CMD ["./deploy_config/entrypoint.sh"]