FROM python:3.7

ENV POETRY_VERSION=1.1.13

WORKDIR /code

RUN pip install "poetry==$POETRY_VERSION"

COPY pyproject.toml poetry.lock ./

RUN poetry export -f requirements.txt --output requirements.txt


RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt



COPY ./ /code/

EXPOSE 8000

CMD ["uvicorn", "service.main:app", "--proxy-headers", "--port", "8000"]