from flask import Flask

server3 = Flask(__name__)

@server3.route('/')
def hello_world():
    return 'Hello from Server 3.\n'

if __name__ == '__main__':
    server3.run(host='0.0.0.0', debug=True)
