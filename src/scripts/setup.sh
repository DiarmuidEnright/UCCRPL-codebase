#!/bin/bash

if ! command -v python3 &> /dev/null
then
    echo "Python3 could not be found. Please install Python3 and rerun the script."
    exit
fi

echo "Creating virtual environment..."
python3 -m venv venv

echo "Activating virtual environment..."
source venv/bin/activate

echo "Upgrading pip..."
pip install --upgrade pip

if [ -f "requirements.txt" ]; then
    echo "Installing Python dependencies..."
    pip install -r requirements.txt
else
    echo "requirements.txt file not found. Please ensure it exists in the project root."
    exit 1
fi

if [ -f ".env.example" ]; then
    echo "Copying .env.example to .env..."
    cp .env.example .env
else
    echo ".env.example not found. Skipping environment setup."
fi

echo "Setup completed successfully. You can now run the application."
