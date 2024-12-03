# Use Python 3.9 base image
FROM python:3.9-slim

# Set environment variables to avoid interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && apt-get install -y \
    sox \
    alsa-utils \
    awscli \
    libhamlib-utils \
    screen \
    python3-pip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy application files into the container
COPY ./app /app

# Install Python dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Expose the Flask API port
EXPOSE 5000

# Command to run the Flask app
CMD ["python3", "main.py"]
