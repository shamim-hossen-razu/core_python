#!/bin/bash

# Shell built-in command
echo "Current directory:"
pwd

# External command
echo "Files in current directory:"
ls -l

# Using type to determine command type
type echo
type ls

# Command substitution with external command
current_date=$(date)
echo "Current date: $current_date"
