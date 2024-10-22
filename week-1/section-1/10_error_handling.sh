#!/bin/bash

# Enable debugging
set -x

# Exit on error
set -e

# Function to handle errors
handle_error() {
    echo "An error occurred on line $1"
    exit 1
}

# Set up error handling
trap 'handle_error $LINENO' ERR

# Intentional error
non_existent_command

# This line won't be executed due to set -e
echo "This won't be printed"
