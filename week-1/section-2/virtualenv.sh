#!/bin/bash

# Install virtualenv if not already installed
pip install virtualenv

# Create a new virtual environment
virtualenv myenv

# Activate the virtual environment
source myenv/bin/activate

# Verify the virtual environment is active
which python
python --version

# Install packages in the virtual environment
pip install package_name

# List installed packages
pip list

# Create requirements.txt
pip freeze > requirements.txt

# Install from requirements.txt
pip install -r requirements.txt

# Deactivate the virtual environment
deactivate

# Remove the virtual environment (optional)
# rm -rf myenv

echo "virtualenv commands completed."
