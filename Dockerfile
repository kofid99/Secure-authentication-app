# Stage 1 — Builder: install dependencies
FROM python:3.11-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir --upgrade jaraco.context==6.1.2 wheel==0.47.0 && \
    pip install --no-cache-dir -r requirements.txt
# Stage 2 — Runtime: lean final image
FROM python:3.11-slim AS runtime

WORKDIR /app

COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages

COPY app.py .

RUN mkdir -p /app/logs && chown -R 1001:1001 /app

USER 1001

EXPOSE 5000

CMD ["python", "app.py"]