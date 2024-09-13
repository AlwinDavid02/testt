# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt ./

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

RUN mkdir /app/logs

# Expose port 5000 for the Flask app
EXPOSE 5001

# Run app.py when the container launches
CMD ["python", "app.py"]
