FROM python:3.12.3

RUN apt-get update && apt-get install -y docker.io

WORKDIR /app

COPY app/load_balancer.py app/consistent_hash.py /app/

RUN pip install flask docker

COPY . .

CMD ["python3", "load_balancer.py"]