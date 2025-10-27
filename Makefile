.PHONY: run test lint migrate
run:
	docker compose up --build
test:
	pytest -q
lint:
	echo "no linter configured"
migrate:
	alembic upgrade head
