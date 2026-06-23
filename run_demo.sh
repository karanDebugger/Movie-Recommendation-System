#!/bin/bash

# Movie Recommendation System - Demo Mode Launcher for Unix

echo ""
echo "🎬 Movie Recommendation System - DEMO MODE"
echo "=========================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

# Check Python version
PYTHON_VERSION=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
echo "✓ Python version: $PYTHON_VERSION"

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "✓ Virtual environment activated"
source venv/bin/activate

# Install/upgrade requirements
echo "📥 Installing dependencies..."
pip install --upgrade pip > /dev/null 2>&1
pip install -r requirements.txt > /dev/null 2>&1

# Run the demo app
echo ""
echo "=========================================="
echo "🚀 Starting Demo App"
echo "=========================================="
echo "📍 Access the app at: http://localhost:5000"
echo "🎯 Try these movies: Avatar, Interstellar, Inception, The Matrix, Gravity"
echo "😄 Bonus: Visit /api/joke for random jokes!"
echo "🛑 Press Ctrl+C to stop"
echo "=========================================="
echo ""

python app_demo.py
