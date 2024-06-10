import aiohttp
import asyncio
import matplotlib.pyplot as plt
from collections import Counter
import requests
import time

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def send_requests(url, num_requests=10000):
    tasks = []
    async with aiohttp.ClientSession() as session:
        for _ in range(num_requests):
            tasks.append(fetch(session, url))
        responses = await asyncio.gather(*tasks)
        return responses

def add_servers(n):
    url = 'http://localhost:5000/add'
    data = {'n': n}
    response = requests.post(url, json=data)
    return response.json()

def measure_load_distribution():
    responses = asyncio.run(send_requests('http://localhost:5000/home'))
    servers = [resp.split(": ")[1].split('"')[0] for resp in responses]
    count = Counter(servers)
    return count

def plot_distribution(count, title, filename):
    plt.bar(count.keys(), count.values())
    plt.xlabel('Server ID')
    plt.ylabel('Number of Requests')
    plt.title(title)
    plt.savefig(f'../plots/{filename}')  # Save the plot
    plt.show()

if __name__ == "__main__":
    for i in range(1, 6):  # Adding servers incrementally from 1 to 5
        add_servers(1)
        time.sleep(10)  # Wait for the server to be fully ready
        count = measure_load_distribution()
        plot_distribution(count, f'Load Distribution with {i + 1} Servers', f'load_distribution_{i + 1}_servers.png')
