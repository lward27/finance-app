FROM python:3.9
USER root
WORKDIR /app

COPY requirements.txt .
COPY src/setup.py .
COPY src/financeapp ./financeapp

RUN pip install -r requirements.txt --user
RUN pip install . --user

LABEL "traefik.http.services.financeapp.loadbalancer.server.port"=8000

EXPOSE 8000

ENTRYPOINT [ "python", "/app/financeapp" ]
