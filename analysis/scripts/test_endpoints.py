import requests
import time

def test_endpoints():
    urls = [
        'http://localhost:5000/rep',
        'http://localhost:5000/add',
        'http://localhost:5000/rm',
        'http://localhost:5000/home',
        'http://localhost:5000/heartbeat'
    ]
    for url in urls:
        response = requests.get(url)
        print(f"GET {url} - Status Code: {response.status_code}, Response: {response.json() if response.content else ''}")

def simulate_failure(server_id):
    container = client.containers.get(server_id)
    container.stop()
    print(f"Server {server_id} stopped.")

if __name__ == "__main__":
    test_endpoints()

    # Simulate failure
    simulate_failure('server1')
    time.sleep(10)  # Wait for the system to detect the failure
    test_endpoints()
