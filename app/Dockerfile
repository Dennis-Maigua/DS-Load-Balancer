FROM python:3.12.3

WORKDIR /app

COPY app/load_balancer.py app/consistent_hash.py /app/

RUN pip install flask docker requests

CMD ["python3", "load_balancer.py"]