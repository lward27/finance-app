FROM python:3.11
USER root
WORKDIR /app

COPY requirements.txt .
COPY src/setup.py .
COPY src/yfinance_wrapper ./yfinance_wrapper

RUN pip install -r requirements.txt --user
RUN pip install . --user

LABEL "traefik.http.services.yfinance_wrapper.loadbalancer.server.port"=80

EXPOSE 80

ENTRYPOINT [ "python", "/app/yfinance_wrapper" ]
