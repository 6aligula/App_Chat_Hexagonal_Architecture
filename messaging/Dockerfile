# Dockerfile for Messaging Service
FROM python:3.9-slim

WORKDIR /app

COPY ./requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 5004

CMD ["python", "domain/services/messaging_service.py"]
