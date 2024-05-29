test:
	@docker compose up --build -d
	@pytest --disable-warnings || true
	@curl http://localhost:5001
	@curl http://localhost:5002
	@curl http://localhost:5003
	@docker compose down