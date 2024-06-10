from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/home', methods=['GET'])
def home():
    server_id = "Server: " + str(app.config['SERVER_ID'])
    return jsonify(message=f"Hello from {server_id}", status="successful"), 200

@app.route('/heartbeat', methods=['GET'])
def heartbeat():
    return '', 200

if __name__ == "__main__":
    import os
    app.config['SERVER_ID'] = os.environ.get('SERVER_ID', '1')
    app.run(host='0.0.0.0', port=5001)
