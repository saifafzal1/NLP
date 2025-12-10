#!/bin/bash

# Knowledge Graph Application - Startup Script
# M.Tech AIML - NLP Applications Assignment 1

echo "========================================"
echo "Knowledge Graph Application"
echo "M.Tech AIML - NLP Applications"
echo "Assignment 1 - PS-9"
echo "========================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed."
    echo "Please install Python 3.8 or higher."
    exit 1
fi

echo "Python version:"
python3 --version
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    echo "Virtual environment created."
    echo ""
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -q -r requirements.txt

if [ $? -eq 0 ]; then
    echo "Dependencies installed successfully."
else
    echo "Error installing dependencies."
    exit 1
fi

echo ""
echo "========================================"
echo "Starting Flask Application..."
echo "========================================"
echo ""
echo "The application will be available at:"
echo "http://127.0.0.1:5000"
echo ""
echo "Press Ctrl+C to stop the server."
echo ""

# Run the Flask application
python3 app.py
