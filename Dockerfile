FROM python:3.11-slim AS base
ENV POETRY_HOME="/opt/poetry" \
    PYTHONUNBUFFERED=1 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    PATH="/root/local/bin:$PATH"

WORKDIR /app
RUN pip install poetry==1.6.1
COPY pyproject.toml poetry.lock ./

FROM base AS local
RUN poetry install -n --no-root

FROM base AS production
COPY . .
RUN poetry install -n --no-dev --no-root
EXPOSE 8000
CMD ["uvicorn", "crowdfooding.src.main:app", "--host", "0.0.0.0", "--port", "8000"]