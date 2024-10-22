#!/bin/bash

# Reading user input
echo "What's your name?"
read user_name

# Displaying output
echo "Hello, $user_name!"

# Using printf for formatted output
printf "Your name has %d characters.\n" ${#user_name}

# Using printf with string format specifier
printf "Your name is: %s\n" "$user_name"

# Redirecting output to a file
echo "This is a log entry" > logfile.txt

# Appending to a file
echo "Another log entry" ${#user_name} >> logfile.txt

# Reading from a file
cat < logfile.txt