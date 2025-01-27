FROM mcr.microsoft.com/vscode/devcontainers/python:3.9

# Install any dependencies
RUN pip install --upgrade pip

# Create a working directory
WORKDIR /workspace

# Copy the current directory contents into the container
COPY . /workspace

# Install any Python dependencies
RUN pip install -r requirements.txt

# Expose port 8888 for Jupyter Notebook
EXPOSE 8888
