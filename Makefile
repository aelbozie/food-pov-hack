all: create_database install_service lint_service test_service run_service build_service
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
	poetry run streamlit run app.py
