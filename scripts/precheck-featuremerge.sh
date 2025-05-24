#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

echo "Running Black formatter on all Python files..."
poetry run black .

echo "Code formatting check completed successfully."
exit 0