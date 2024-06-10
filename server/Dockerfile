FROM python:3.12.3

WORKDIR /app

COPY server/server.py /app

RUN pip install flask

COPY . /app

ENV SERVER_ID=1

CMD ["python3", "server.py"]
