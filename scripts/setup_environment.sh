#!/bin/bash

# Workshop Git Environment Setup Script
# This script helps set up the Python environment for the workshop

echo "========================================="
echo "Git & GitHub Workshop - Environment Setup"
echo "========================================="
echo ""

# Check Python version
echo "Checking Python version..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version)
    echo "Found: $PYTHON_VERSION"
else
    echo "Error: Python 3 is not installed!"
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo ""
    echo "Creating virtual environment..."
    python3 -m venv venv
    echo "Virtual environment created successfully!"
else
    echo ""
    echo "Virtual environment already exists."
fi

# Activate virtual environment and install dependencies
echo ""
echo "To activate the virtual environment, run:"
echo "  source venv/bin/activate"
echo ""
echo "Then install dependencies with:"
echo "  pip install -r requirements.txt"
echo ""
echo "Setup complete!"
