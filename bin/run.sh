#!/usr/bin/env bash

export INITIALISE_WITH_MOCK_DATA=1
export FASTAPI_PORT=${PORT:-8000}
export STREAMLIT_PORT=${PORT:-8001}

uvicorn service.main:app --proxy-headers --port $FASTAPI_PORT --host 0.0.0.0 &
streamlit run app/1_Food_to_Bank.py --server.port $STREAMLIT_PORT --server.address 0.0.0.0
