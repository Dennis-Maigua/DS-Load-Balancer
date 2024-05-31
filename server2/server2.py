from flask import Flask

server2 = Flask(__name__)

@server2.route('/')
def hello_world():
    return 'Hello from Server 2.\n'

if __name__ == '__main__':
    server2.run(host='0.0.0.0', debug=True)
