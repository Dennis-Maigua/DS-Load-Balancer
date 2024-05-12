# Load Balancer within a Docker Network

![Load Balancer](https://github.com/Dennis-Maigua/DS-Load-Balancer/assets/32156551/39a184e9-217b-4c3c-93f9-52b5281dcd28)

# Design

A load balancer is used to route the requests coming from several clients asynchronously among several servers, so that the load is nearly evenly distributed among them. To scale a particular service with increasing clients, it manages multiple replicas of the service to improve resource utilization and throughput. It uses a consistent hashing data structure to distribute the requests coming from the clients efficiently. There should always be servers present to handle the requests. In the event of failure of a server, the load balancer spawns new replicas of the server to handle the requests.

# Assumptions

1. You are running Linux Ubuntu v20.04 or above on a host/virtual machine.

2. You have installed python3 and pip3 libraries. Use the following commands to install:

   ```
   $ sudo apt-get update
   $ sudo apt-get install python3 python3-pip python3-pytest -y
   $ python3 --version
   $ pip3 --version
   ```
   
3. You have installed docker packages. Use the following commands to install:
  
   ```
   $ sudo apt-get install docker -y
   $ sudo apt-get install ca-certificates curl
   $ sudo install -m 0755 -d /etc/apt/keyrings
   $ sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
   $ sudo chmod a+r /etc/apt/keyrings/docker.asc
    
   # Add the repository to Apt sources:
   $ echo \
      "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
      $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
      sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
   
   $ sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
   $ sudo apt-get update
   ```
   
4. You have installed git. Use the following commands to install:
  
   ```
   $ sudo apt install git
   $ git --version
   $ sudo apt update
   $ git config --global user.name "Your Name"
   $ git config --global user.email "youremail@domain.com"
   $ git config --list
   ```

# Installation

1. Open a new terminal on Linux Ubuntu and clone the Github repository.

  ```
  $ git clone https://github.com/Dennis-Maigua/DS-Load-Balancer.git
  ```

2. Open the cloned project folder/directory e.g. /Desktop/DS-Load-Balancer.

  ```
  $ cd Desktop/DS-Load-Balancer
  ```

3. Run the following commands:

  ```
  $ docker build -t server .
  $ docker images
  $ docker tag server:latest dsloadbal.azurecr.io/lb:v1
  $ docker images
  $ docker login dsloadbal.azurecr.io
  Username: dsloadbal
  Password: pass
  $ docker push dsloadbal.azurecr.io/lb:v1
  $ docker run server:latest
  $ docker compose up -d 
  ```

# Testing and Performance

  ```
  $ curl localhost:5001
  $ curl localhost:5002
  $ curl localhost:5003
  $ docker compose down
  ```
  
