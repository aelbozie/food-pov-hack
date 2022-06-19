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
	docker build . -t foodhack:latest

run_service: build_service
	docker run -p 8000:8000 -ti foodhack:latest 

