# Use the official Python image as a base
FROM python:3.9-slim

# Set a working directory inside the container
WORKDIR /app

# Copy requirements.txt to the working directory
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install Jupyter and other necessary tools
RUN pip install jupyterlab

# Install additional packages required for testing and linting
RUN pip install flake8 pytest nbval

# Copy the entire project into the working directory
COPY . .

# Set environment variables (optional, if you have any credentials or settings)
ENV PYTHONUNBUFFERED=1

# Expose the Jupyter Notebook port
EXPOSE 8888

# Command to run Jupyter Lab
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
