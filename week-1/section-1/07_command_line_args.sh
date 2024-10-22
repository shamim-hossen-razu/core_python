#!/bin/bash

# # Accessing command-line arguments
# echo "Script name: $0"
# echo "First argument: $1"
# echo "Second argument: $2"
# echo "All arguments: $@"

# # Using getopts for option parsing
# while getopts ":a:b:" opt; do
#   case $opt in
#     a) echo "Option -a was triggered, Parameter: $OPTARG" ;;
#     b) echo "Option -b was triggered, Parameter: $OPTARG" ;;
#     \?) echo "Invalid option: -$OPTARG" ;;
#   esac
done

#!/bin/bash

# Default values
name=""
age=""

# Parse command-line options
while getopts ":n:a:" opt; do
  case $opt in
    n) name="$OPTARG" ;;
    a) age="$OPTARG" ;;
    \?) echo "Invalid option: -$OPTARG" >&2; exit 1 ;;
    :) echo "Option -$OPTARG requires an argument." >&2; exit 1 ;;
  esac
done

# Check if required options are provided
if [ -z "$name" ] || [ -z "$age" ]; then
  echo "Usage: $0 -n <name> -a <age>"
  exit 1
fi

# Use the provided arguments
echo "Hello, $name! You are $age years old."

# Additional logic based on age
if [ "$age" -lt 18 ]; then
  echo "You are a minor."
elif [ "$age" -ge 18 ] && [ "$age" -lt 65 ]; then
  echo "You are an adult."
else
  echo "You are a senior citizen."
fi
