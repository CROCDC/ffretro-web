FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=run.py
ENV FLASK_DEBUG=0

RUN mkdir -p /app/uploads && chown -R nobody:nogroup /app/uploads
EXPOSE 7012

USER nobody
CMD ["flask", "run", "--host=0.0.0.0", "--port=7012"]
