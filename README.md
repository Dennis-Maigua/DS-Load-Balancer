[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the MIT license.

# Customizable Load Balancer

![Load Balancer](https://github.com/Dennis-Maigua/DS-Load-Balancer/assets/32156551/39a184e9-217b-4c3c-93f9-52b5281dcd28)

This project implements a customizable load balancer using consistent hashing.

## Design

1. **Server:** Simple Docker server with `/home` and `/heartbeat` endpoints.
2. **Consistent Hashing:** Python implementation of consistent hashing.
3. **Load Balancer:** Flask-based load balancer managing server containers.

## Setup

1. Install `python3`, `pip`, and `pytest` libraries:

   ```bash
   $ sudo apt-get update
   $ sudo apt-get install python3 python3-pip python3-pytest -y
   $ python3 --version
   $ pip --version
   $ pytest --version
   ```
   
2. Install `docker` & `docker-compose` packages:
  
   ```bash
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
   
3. Install and configure `git`:
  
   ```bash
   $ sudo apt install git
   $ git --version
   $ sudo apt update
   $ git config --global user.name "your-github-username"
   $ git config --global user.email "your-github-email"
   $ git config --list
   ```

4. Clone the repository and open the project folder/directory:

  ```bash
  $ git clone https://github.com/Dennis-Maigua/DS-Load-Balancer.git
  $ cd Desktop/DS-Load-Balancer
  ```

## Testing and Performance

1. Build and Run docker images or containers:

  ```bash
  $ make all
  ```

![Screenshot from 2024-06-13 13-10-38](https://github.com/Dennis-Maigua/DS-Load-Balancer/assets/32156551/f3d34404-de3b-437f-a8ff-89f4cc05256c)

2. Open a new terminal and install dependencies:

  ```bash
  $ sudo apt-get install python3-aiohttp python3-matplotlib -y
  ```

3. Run asynchronous requests and plot a load distribution graph of the responses:

  ```bash
  $ cd analysis/scripts
  $ python3 async_requests.py
  ```

4. Add Servers and Measure Load Distribution:

  ```bash
  $ python3 incremental_servers.py
  ```

5. Test Endpoints and Observe Failures:

  ```bash
  $ python3 test_endpoints.py
  ```

6. Compare Different Hash Functions:

  ```bash
  $ python3 compare_hash_functions.py
  ```
