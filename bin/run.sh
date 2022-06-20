#!/usr/bin/env bash

export INITIALISE_WITH_MOCK_DATA=1
export FASTAPI_PORT=${PORT:-8000}
export STREAMLIT_PORT=${PORT:-8001}

rm -f data/inventory.db

uvicorn service.main:app --proxy-headers --port $FASTAPI_PORT --host 0.0.0.0 &
PYTHONPATH="." streamlit run web/1_Barcode_Scanner.py --server.port $STREAMLIT_PORT --server.address 0.0.0.0
