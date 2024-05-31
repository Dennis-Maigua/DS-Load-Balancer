test:
	@docker pull ealen/echo-server
	@docker compose up -d --build
	@docker ps
	@docker compose logs -f server-1
	@docker compose logs -f server-2
	@docker compose logs -f server-3
	@watch -n 1 curl -s localhost:9999
	@docker rm -f ds-load-balancer-server-3-1
	@docker compose down