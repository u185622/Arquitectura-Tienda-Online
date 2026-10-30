FROM python:3.12-slim

WORKDIR /app

COPY Tienda_online/ .

CMD ["python", "main.py"]
