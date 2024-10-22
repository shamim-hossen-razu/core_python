#!/bin/bash

# If-else statement
age=18
if [ $age -ge 18 ]; then
    echo "You are an adult."
else
    echo "You are a minor."
fi

# Case statement
fruit="apple"
case $fruit in "apple") echo "It's an apple.";;
    "banana") echo "It's a banana.";;
    *) echo "Unknown fruit.";;
esac

# For loop
for i in {1..5}; do
    echo "Iteration $i"
done

# While loop
count=0
while [ $count -lt 3 ]; do
    echo "Count: $count"
    ((count++))
done

# Demonstrating break and continue in loops

# Using break in a loop
echo "Demonstrating break:"
for i in {1..10}; do
    if [ $i -eq 5 ]; then
        echo "Breaking at $i"
        break
    fi
    echo "Iteration $i"
done

# Using continue in a loop
echo -e "\nDemonstrating continue:"
for i in {1..5}; do
    if [ $i -eq 3 ]; then
        echo "Skipping iteration $i"
        continue
    fi
    echo "Iteration $i"
done

# Using break in a while loop
echo -e "\nDemonstrating break in while loop:"
counter=0
while true; do
    ((counter++))
    echo "Counter: $counter"
    if [ $counter -eq 5 ]; then
        echo "Breaking the loop"
        break
    fi
done

# Using continue in a while loop
echo -e "\nDemonstrating continue in while loop:"
counter=0
while [ $counter -lt 5 ]; do
    ((counter++))
    if [ $((counter % 2)) -eq 0 ]; then
        echo "Skipping even number: $counter"
        continue
    fi
    echo "Odd number: $counter"
done

# Demonstrating range in Bash

# Using seq command to generate a range
echo "Range using seq:"
for i in $(seq 1 5); do
    echo "Number: $i"
done

# Using brace expansion for range
echo -e "\nRange using brace expansion:"
for i in {1..5}; do
    echo "Number: $i"
done

# Using C-style for loop for range
echo -e "\nRange using C-style for loop:"
for ((i=1; i<=5; i++)); do
    echo "Number: $i"
done

# Range with step using seq
echo -e "\nRange with step using seq:"
for i in $(seq 0 2 10); do
    echo "Number: $i"
done

# Range with step using brace expansion
echo -e "\nRange with step using brace expansion:"
for i in {0..10..2}; do
    echo "Number: $i"
done

