#!/bin/bash

# Movie Recommendation System - Quick Start Script

echo "🎬 Movie Recommendation System - Startup"
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

# Check if Artifacts directory exists
if [ ! -d "Artifacts" ]; then
    echo "⚠️  Creating Artifacts directory..."
    mkdir -p Artifacts
    echo "   Place your data files here:"
    echo "   - main_data.csv (movie dataset)"
    echo "   - nlp_model.pkl (sentiment model)"
    echo "   - transform.pkl (vectorizer)"
fi

# Run the app
echo ""
echo "=========================================="
echo "🚀 Starting Movie Recommendation System"
echo "=========================================="
echo "📍 Access the app at: http://localhost:5000"
echo "🛑 Press Ctrl+C to stop"
echo "=========================================="
echo ""

python app.py
