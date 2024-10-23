#!/bin/bash

# Install pyenv dependencies
sudo apt-get update
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl

# Install pyenv
curl https://pyenv.run | bash

# Add pyenv to PATH and initialize
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init --path)"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
source ~/.bashrc

# Install Python versions
pyenv install 3.8.12
pyenv install 3.9.7

# Set global Python version
pyenv global 3.9.7

# Create a virtual environment
pyenv virtualenv 3.9.7 myproject

# Activate the virtual environment
pyenv activate myproject

# Install packages in the virtual environment
pip install package_name

# List installed packages
pip list

# Create requirements.txt
pip freeze > requirements.txt

# Deactivate the virtual environment
pyenv deactivate

# List installed Python versions
pyenv versions

# Uninstall a Python version (optional)
# pyenv uninstall 3.8.12

echo "pyenv setup and commands completed."
