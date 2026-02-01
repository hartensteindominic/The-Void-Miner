#!/bin/bash
# Build script for The Void Miner

set -e

echo "Building The Void Miner..."

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Install the package in development mode
echo "Installing package in development mode..."
pip install -e .

echo "Build completed successfully!"
echo ""
echo "To run the game:"
echo "  source venv/bin/activate"
echo "  void-miner"
echo ""
echo "Or:"
echo "  python -m void_miner"
