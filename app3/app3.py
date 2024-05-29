from flask import request, Flask

app3 = Flask(__name__)

@app3.route('/')
def hello_world():
    return 'Hello from Server 3.\n'

if __name__ == '__main__':
    app3.run(host='0.0.0.0', debug=True)
