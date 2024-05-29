from flask import request, Flask

app1 = Flask(__name__)

@app1.route('/')
def hello_world():
    return 'Hello from Server 1.\n'

if __name__ == '__main__':
    app1.run(host='0.0.0.0', debug=True)
