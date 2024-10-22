#!/bin/bash

# Creating a directory
mkdir test_dir

# Creating a file
touch test_dir/test_file.txt

# Writing to a file
echo "Hello, File!" > test_dir/test_file.txt

# Reading from a file
cat test_dir/test_file.txt

# Checking if a file exists
if [ -f test_dir/test_file.txt ]; then
    echo "File exists"
fi

# Changing file permissions
chmod 755 test_dir/test_file.txt

# Removing a file
rm test_dir/test_file.txt

# Removing a directory
rmdir test_dir
