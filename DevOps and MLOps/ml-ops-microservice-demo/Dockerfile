# Use Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy files
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .

# Expose port
EXPOSE 5000

# Start app
CMD ["python", "app.py"]
