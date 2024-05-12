test:
	@docker compose up -d
	@pytest --disable-warnings || true
	@curl http://172.17.0.1:5001
	@curl http://172.17.0.1:5002
	@curl http://172.17.0.1:5003
	@curl http://localhost:80
	@docker compose down