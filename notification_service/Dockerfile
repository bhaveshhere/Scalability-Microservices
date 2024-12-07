# FROM python:3.9-slim

# WORKDIR /app

# COPY requirements.txt .
# RUN pip install -r requirements.txt

# COPY . .

# EXPOSE 8002

# CMD ["uvicorn", "notification_service:app", "--host", "0.0.0.0", "--port", "8004"]
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Expose port 8002 to map to the local machine's port (for communication outside the container)
EXPOSE 8004

# Run the FastAPI application on port 8004 inside the container
CMD ["uvicorn", "notification_service:app", "--host", "0.0.0.0", "--port", "8004"]
