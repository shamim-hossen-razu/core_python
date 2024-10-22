#!/bin/bash

# Regular array
fruits=("apple" "banana" "cherry")
echo "Second fruit: ${fruits[1]}"

# Looping through array
for fruit in "${fruits[@]}"; do
    echo "Fruit: $fruit"
done

# Associative array (Bash 4.0+)
declare -A user_info
user_info[name]="John"
user_info[age]=30

echo "Name: ${user_info[name]}"
echo "Age: ${user_info[age]}"
