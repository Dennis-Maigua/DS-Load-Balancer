# Dockerfile for the server
FROM python:3.12.3

# Set the working directory in the container
RUN mkdir /app
WORKDIR /app/
ADD . /app/

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install dependencies
RUN pip3 install -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . .

# Expose the port on which the Flask app will run
EXPOSE 5000

# Command to run the Flask application
CMD ["python3", "/app/app.py"]
