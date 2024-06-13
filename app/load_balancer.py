from flask import Flask, request, jsonify
import docker
import random
import requests
from consistent_hash import ConsistentHash

app = Flask(__name__)
docker_client = docker.from_env()
hash_map = ConsistentHash()

# Initial servers
servers = ["server1", "server2", "server3"]
for server in servers:
    hash_map.add_node(server)

@app.route('/rep', methods=['GET'])
def get_replicas():
    return jsonify({"replicas": list(hash_map.nodes.values()), "status": "successful"}), 200

@app.route('/add', methods=['POST'])
def add_replicas():
    data = request.json
    num_instances = data['n']
    hostnames = data.get('hostnames', [])
    
    for i in range(num_instances):
        hostname = hostnames[i] if i < len(hostnames) else f"server{random.randint(1000, 9999)}"
        container = docker_client.containers.run('simple-server', detach=True, environment={"SERVER_ID": hostname})
        hash_map.add_node(hostname)

    return jsonify({"message": {"N": len(hash_map.nodes), "replicas": list(hash_map.nodes.values())}, "status": "successful"}), 200

@app.route('/rm', methods=['DELETE'])
def remove_replicas():
    data = request.json
    num_instances = data['n']
    hostnames = data.get('hostnames', [])
    
    for i in range(num_instances):
        hostname = hostnames[i] if i < len(hostnames) else random.choice(list(hash_map.nodes.values()))
        container = docker_client.containers.get(hostname)
        container.stop()
        container.remove()
        hash_map.remove_node(hostname)

    return jsonify({"message": {"N": len(hash_map.nodes), "replicas": list(hash_map.nodes.values())}, "status": "successful"}), 200

@app.route('/<path:path>', methods=['GET'])
def route_request(path):
    server = hash_map.get_node(path)
    response = requests.get(f"http://{server}:5000/{path}")
    return response.content, response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
