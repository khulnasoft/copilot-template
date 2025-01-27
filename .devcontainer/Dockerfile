FROM mcr.microsoft.com/vscode/devcontainers/python:3.9

# Install any dependencies
RUN pip install --upgrade pip

# Create a working directory
WORKDIR /workspace

# Copy the current directory contents into the container
COPY . /workspace

# Install any Python dependencies
RUN pip install -r requirements.txt

# Expose port 5000 for the Flask app
EXPOSE 5000
