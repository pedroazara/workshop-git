#!/bin/bash

# Script to run all tests with coverage

echo "Running tests with coverage..."
echo ""

# Activate virtual environment
source venv/bin/activate

# Run pytest with coverage
pytest tests/ --cov=src --cov-report=html --cov-report=term

echo ""
echo "Coverage report generated in htmlcov/index.html"
