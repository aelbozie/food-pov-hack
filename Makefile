all: create_database install lint test run_service run_app build run
.PHONY: all

install:
	poetry install

lint:
	poetry run isort web service tests
	poetry run black web service tests
	poetry run flake8 web service tests

test:
	poetry run pytest tests

run_service:
	poetry run uvicorn service.main:app --reload

run_app:
	poetry run bin/run.sh

build:
	docker build -f Dockerfile.python . -t foodhack:latest

run: build
	docker run -p 8001:8001 -ti foodhack:latest

