FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    cron \
    && apt install -y jq

RUN apt-get update && apt-get install -y python3

WORKDIR /app
RUN mkdir processos/
RUN mkdir processos/rotinas/

COPY .env /app/
COPY usuarios.json /app/
COPY constants /app/constants
COPY helpers /app/helpers
COPY requirements.txt /app/
COPY entrypoint.sh /app/
COPY start.sh /app/
COPY consulta_processo.py /app/
COPY main.py /app/
COPY consulta_processo.py /app/ 
COPY notifica.py /app/

RUN pip install --no-cache-dir -r requirements.txt
RUN playwright install
RUN playwright install-deps

RUN chmod +x /app/start.sh

CMD ["/app/start.sh"]