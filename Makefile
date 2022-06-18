.PHONY: create_database install_service run_service lint_service test_service

create_database:
	poetry run bin/populate_database.py

install_service:
	poetry install

run_service:
	poetry run uvicorn service.main:app --reload

lint_service:
	poetry run isort service
	poetry run black service
	poetry run flake8 service

test_service:
	poetry run pytest tests/service

