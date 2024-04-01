# Description: Dockerfile for the application
# Author: Dipesh Ghag
FROM python:3.10-alpine

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install updates and awscli
RUN apt update && apt install awscli -y

# Install the required packages
RUN pip install -r requirements.txt

# Run the application
CMD ["python3", "app.py"]