#!/bin/bash

# Use meaningful variable names
user_name="John Doe"

# Use constants for fixed values
readonly MAX_ATTEMPTS=3

# Function names should be lowercase with underscores
calculate_average() {
    local sum=0
    local count=0
    for num in "$@"; do
        sum=$((sum + num))
        ((count++))
    done
    echo $((sum / count))
}

# Always quote variables
echo "User: $user_name"

# Use [[ ]] for conditional tests
if [[ $user_name == "John Doe" ]]; then
    echo "Hello, John!"
fi

# Main script logic
main() {
    local avg=$(calculate_average 10 20 30)
    echo "Average: $avg"
}

# Call main function
main
