from flask import request, Flask

server1 = Flask(__name__)

@server1.route('/')
def hello_world():
    return 'Hello from Server 1.\n'

if __name__ == '__main__':
    server1.run(host='0.0.0.0', debug=True)
