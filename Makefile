all: build up

build:
	docker compose build

up:
	docker compose up -d

test: 
	docker ps

remove:
	docker rmi -f $(docker images -aq)

down:
	docker compose down --rmi all
