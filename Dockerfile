# Use official Python image as base
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y build-essential default-libmysqlclient-dev gcc pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Copy project files
COPY . /app/

# Expose port (Gunicorn default or Flask dev)
EXPOSE 5001

# Set environment variable for Flask
ENV FLASK_APP=run.py

# Run the application with Gunicorn
CMD ["gunicorn", "run:app", "--bind", "0.0.0.0:5001"] 