all: build up

build:
	docker compose build

up:
	docker compose up -d

test: 
	docker ps

remove:
	docker rm -vf $(docker ps -aq)
	docker rmi -f $(docker images -aq)
	docker system prune -a --volumes -y

down:
	docker compose down --rmi all
