# FROM python:3.9-slim

# WORKDIR /app

# COPY requirements.txt .
# RUN pip install -r requirements.txt

# COPY . .

# EXPOSE 8001

# CMD ["uvicorn", "follow_service:app", "--host", "0.0.0.0", "--port", "8003"]
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Expose port 8003
EXPOSE 8003

# Set the command to run the FastAPI app with Uvicorn on port 8003
CMD ["uvicorn", "follow_service:app", "--host", "0.0.0.0", "--port", "8003"]

