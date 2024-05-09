# Dockerfile for the server
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . .

# Expose the port on which the Flask app will run
EXPOSE 5000

# Command to run the Flask application
CMD ["python", "app.py"]
