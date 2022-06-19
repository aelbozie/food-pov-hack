all: create_database install_service run_service lint_service test_service
.PHONY: all

create_database:
	poetry run bin/create_database.py

install_service:
	poetry install

lint_service:
	poetry run isort service
	poetry run black service
	poetry run flake8 service

test_service:
	poetry run pytest tests/service

run_service:
	poetry run uvicorn service.main:app --reload


