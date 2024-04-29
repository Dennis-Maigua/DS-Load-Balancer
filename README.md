# Load Balancer within a Docker Network

![Load Balancer](https://github.com/Dennis-Maigua/DS-Load-Balancer/assets/32156551/39a184e9-217b-4c3c-93f9-52b5281dcd28)

A load balancer routes the requests coming from several clients asynchronously among several servers so that the load is nearly evenly distributed among them. To scale a particular service with increasing clients, load balancers are used to manage multiple replicas of the service to improve resource utilization and throughput. A load balancer uses a consistent hashing data structure to distribute the requests coming from the clients efficiently. There should always be servers present to handle the requests. In the event of failure, new replicas of the server will be spawned by the load balancer to handle the requests.

# Design

# Assumptions

# Testing and performance analysis
