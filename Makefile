all: build up

build:
	docker compose build

up:
	docker compose up

test: 
	docker ps

remove:
	docker rm -f ds-load-balancer-server1
	docker rm -f ds-load-balancer-server2
	docker rm -f ds-load-balancer-server3
	docker rm -f ds-load-balancer-load_balancer

down:
	docker compose down
