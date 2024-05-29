from flask import request, Flask

app2 = Flask(__name__)

@app2.route('/')
def hello_world():
    return 'Hello from Server 2.\n'

if __name__ == '__main__':
    app2.run(host='0.0.0.0', debug=True)
