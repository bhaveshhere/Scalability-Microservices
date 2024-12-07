FROM python:3.9-slim

WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the application code
COPY . .

# Expose port 8001 (service will be running on this port)
EXPOSE 8007

# Run the FastAPI application
CMD ["uvicorn", "user_service:app", "--host", "0.0.0.0", "--port", "8007"]

