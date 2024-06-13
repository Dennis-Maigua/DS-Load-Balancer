from flask import Flask, request, jsonify
import docker
from consistent_hash import ConsistentHash

app = Flask(__name__)
client = docker.from_env()
chash = ConsistentHash()

@app.route('/rep', methods=['GET'])
def get_replicas():
    replicas = list(chash.nodes.values())
    return jsonify(message={"N": len(replicas), "replicas": replicas}, status="successful"), 200

@app.route('/add', methods=['POST'])
def add_replicas():
    data = request.json
    num_instances = data['n']
    hostnames = data.get('hostnames', [])
    new_replicas = []

    for i in range(num_instances):
        hostname = hostnames[i] if i < len(hostnames) else f"Server-{len(chash.nodes) + i}"
        container = client.containers.run('server_image', environment={"SERVER_ID": hostname}, detach=True)
        new_replicas.append(hostname)
        chash.add_node(hostname)

    return jsonify({"message": {"N": len(chash.nodes), "replicas": list(chash.nodes.values())}, "status": "successful"}), 200

@app.route('/rm', methods=['DELETE'])
def remove_replicas():
    data = request.json
    num_instances = data['n']
    hostnames = data.get('hostnames', [])
    
    for i in range(num_instances):
        hostname = hostnames[i] if i < len(hostnames) else None
        if hostname:
            chash.remove_node(hostname)
            container = client.containers.get(hostname)
            container.stop()
            container.remove()

    return jsonify({"message": {"N": len(chash.nodes), "replicas": list(chash.nodes.values())}, "status": "successful"}), 200

@app.route('/<path:path>', methods=['GET'])
def route_request(path):
    server = chash.get_node(path)
    response = client.containers.get(server).exec_run(f"curl http://{server}:5000/{path}")
    return response.output, response.exit_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
