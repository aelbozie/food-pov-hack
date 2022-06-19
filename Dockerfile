FROM python:3.8

ENV POETRY_VERSION=1.1.13

WORKDIR /code

RUN pip install "poetry==$POETRY_VERSION"

COPY ./ ./

RUN poetry config virtualenvs.create false && \
    poetry config virtualenvs.in-project false && \
    poetry install 

ENV PORT 8000

CMD uvicorn service.main:app --proxy-headers --port $PORT --host 0.0.0.0