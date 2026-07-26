FROM python:3.11-slim
WORKDIR /app
RUN apt-get update && apt-get install -y libpq-dev gcc && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD gunicorn app:app --bind 0.0.0.0:$PORT
# force rebuild Sun 26 Jul 2026 13:44:36 BST
