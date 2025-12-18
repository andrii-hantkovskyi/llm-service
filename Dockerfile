FROM python:3.13-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# Install dependencies
# --frozen: strict sync from uv.lock
# --no-dev: excludes test/lint dependencies
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev

COPY app ./app

ENV PATH="/app/.venv/bin:$PATH"

CMD ["fastapi", "run", "app/main.py", "--port", "80", "--host", "0.0.0.0"]
