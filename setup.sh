#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Step 1: Create and activate a virtual environment (optional but recommended)
echo "Creating virtual environment..."
python3 -m venv venv

echo "Activating virtual environment..."
source venv/bin/activate

# Step 2: Upgrade pip to the latest version
echo "Upgrading pip..."
pip install --upgrade pip

# Step 3: Install the required dependencies
echo "Installing required packages..."
pip install -r requirements.txt

# Step 4: Set up Jupyter Lab (if needed)
echo "Setting up Jupyter Lab..."
jupyter labextension install @jupyter-widgets/jupyterlab-manager

# Step 5: Run initial tests to verify setup
echo "Running tests to verify the setup..."
pytest test_lib.py test_main.py

# Final message
echo "Setup is complete. You can now activate the virtual environment using 'source venv/bin/activate' and start working on the project."
