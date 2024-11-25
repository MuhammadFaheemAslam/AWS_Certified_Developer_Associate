# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Flask application code into the container
COPY Flask_App /app

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Expose port 5000 for Flask
EXPOSE 5000

# Run Flask app
CMD ["python", "/app/app.py"]
