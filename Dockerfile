# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the necessary dependencies
RUN pip install --no-cache-dir flask

# Expose port 5000 for the Flask app
EXPOSE 5000

# Set environment variable for Flask app
ENV FLASK_APP=app.py

# Run the Flask app
CMD ["python3", "app.py"]
