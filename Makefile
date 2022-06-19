all: create_database install_service lint_service test_service run_app build run
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

run_app:
	poetry run streamlit run app/1_Food_to_Bank.py

build:
	docker build -f Dockerfile.python . -t foodhack:latest

run: build
	docker run -p 8001:8001 -ti foodhack:latest

