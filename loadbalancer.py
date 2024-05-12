import random
import requests
from flask import Flask, request

loadbalancer = Flask(__name__)

SERVERS = ['localhost:5001', 'localhost:5002','localhost:5003']

@loadbalancer.route('/')
def router():
    host_header = request.headers['Host']
    if host_header == 'www.myservers.com':
        response = requests.get(f'http://{random.choice(SERVERS)}')
        return response.content, response.status_code
    else:
        return 'Not Found', 404