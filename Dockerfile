# Dockerfile
FROM python:3.9-slim

WORKDIR /app

# Copy files
COPY server/requirements.txt . 

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

COPY server/ /app/

# Expose the port
EXPOSE 8000

# Run the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
