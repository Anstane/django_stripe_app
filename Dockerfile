FROM python:3.11-slim
WORKDIR /app
RUN pip install poetry==1.7.0
COPY poetry.lock pyproject.toml ./
RUN poetry install --no-interaction --no-ansi
COPY . ./