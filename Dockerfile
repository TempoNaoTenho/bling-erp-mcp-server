FROM python:3.14-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY pyproject.toml README.md LICENSE .
COPY bling_mcp ./bling_mcp
COPY bling-openapi-reference.md ./bling-openapi-reference.md
COPY bling-openapi.json ./bling-openapi.json

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir .

RUN useradd -ms /bin/bash app \
    && chown -R app:app /app

USER app

EXPOSE 3333

CMD ["python", "-m", "bling_mcp"]
