all: create_database install_service run_service lint_service test_service
.PHONY: all

install_service:
	poetry install

lint_service:
	poetry run isort service tests
	poetry run black service tests
	poetry run flake8 service tests

test_service:
	poetry run pytest tests/service

run_service:
	poetry run uvicorn service.main:app --reload

build_service:
	docker build -f Dockerfile.python . -t foodhack-backend:latest

run_service: build_service
	docker run -p 8000:8000 -ti foodhack-backend:latest

build_frontend:
	docker build -f Dockerfile.node . -t foodhack-frontend:latest

run_frontend: build_frontend
	docker run -p 3000:3000 -ti foodhack-frontend:latest
