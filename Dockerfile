# Dockerfile for the server
FROM python:3.12.3

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install dependencies
RUN pip3 install -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . .

# Command to run the Flask application
CMD ["python3", "app.py"]
