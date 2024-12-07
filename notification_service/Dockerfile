FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8002

CMD ["uvicorn", "notification_service:app", "--host", "0.0.0.0", "--port", "8004"]
