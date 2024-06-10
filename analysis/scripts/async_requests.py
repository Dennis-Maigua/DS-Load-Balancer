import aiohttp
import asyncio
import matplotlib.pyplot as plt
from collections import Counter

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    url = 'http://localhost:5000/home'
    tasks = []

    async with aiohttp.ClientSession() as session:
        for _ in range(10000):
            tasks.append(fetch(session, url))

        responses = await asyncio.gather(*tasks)
        return responses

if __name__ == "__main__":
    responses = asyncio.run(main())
    servers = [resp.split(": ")[1].split('"')[0] for resp in responses]  # Extract server IDs
    count = Counter(servers)

    # Plotting the load distribution
    plt.bar(count.keys(), count.values())
    plt.xlabel('Server ID')
    plt.ylabel('Number of Requests')
    plt.title('Load Distribution among Servers')
    plt.savefig('../plots/load_distribution_1_server.png')  # Save the plot
    plt.show()
