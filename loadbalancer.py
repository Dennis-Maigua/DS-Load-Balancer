import asyncio
import random

class LoadBalancer:
    def __init__(self, servers):
        self.servers = servers
        self.current_index = 0

    async def handle_request(self, reader, writer):
        server = await self.get_server()
        await server.send_response(reader, writer)

    async def get_server(self):
        server = self.servers[self.current_index]
        self.current_index = (self.current_index + 1) % len(self.servers)
        return server

    async def health_check(self):
        while True:
            for server in self.servers:
                if not await server.check_health():
                    print(f"Server {server.name} is unhealthy. Removing from rotation.")
                    self.servers.remove(server)
                    # Spawn a new replica to replace the failed server
                    # This is just a placeholder. You should implement this logic using Docker's API.
                    self.spawn_replica(server)
            await asyncio.sleep(5)  # Health check interval

    def spawn_replica(self, failed_server):
        print(f"Spawning new replica for {failed_server.name}")

class Server:
    def __init__(self, name, host, port):
        self.name = name
        self.host = host
        self.port = port
        self.is_healthy = True

    async def send_response(self, reader, writer):
        response = b'HTTP/1.1 200 OK\r\n\r\nSuccess!'
        writer.write(response)
        await writer.drain()
        writer.close()

    async def check_health(self):
        # Simulating health check based on the server's health check mechanism.
        return random.choice([True, False])  

async def main():
    servers = [
        Server('server1', 'localhost', 5001),
        Server('server2', 'localhost', 5002),
        Server('server3', 'localhost', 5003)
    ]  # Example servers
    load_balancer = LoadBalancer(servers)

    health_check_task = asyncio.create_task(load_balancer.health_check())
    
    server = await asyncio.start_server(load_balancer.handle_request, '0.0.0.0', 8080)

    async with server:
        await server.serve_forever()

asyncio.run(main())
