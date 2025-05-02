#!/bin/bash

# Determine project root
if [[ $(basename $(pwd)) == "scripts" || $(basename $(pwd)) == "server" ]]; then
    PROJECT_ROOT=$(pwd)/..
else
    PROJECT_ROOT=$(pwd)
fi

# Activate virtual environment
if [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "win32" ]]; then
    source "$PROJECT_ROOT/venv/Scripts/activate" || . "$PROJECT_ROOT/venv/Scripts/activate"
else
    source "$PROJECT_ROOT/venv/bin/activate" || . "$PROJECT_ROOT/venv/bin/activate"
fi
# Check if the virtual environment is activated
if [[ "$VIRTUAL_ENV" == "" ]]; then
    echo "Virtual environment is not activated. Please run setup-env.sh first."
    exit 1
fi
# Check if the server directory exists
if [[ ! -d "$PROJECT_ROOT/server" ]]; then
    echo "Server directory does not exist. Please run setup-env.sh first."
    exit 1
fi

# Run server tests
cd "$PROJECT_ROOT/server" || exit 1
echo "Running server tests..."

# Check if windows or linux/mac
if [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "win32" ]]; then
    py -m unittest discover -s tests -p "*.py"
else
    python3 -m unittest discover -s tests -p "*.py"
fi