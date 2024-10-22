#!/bin/bash

# Declaring and using variables
name="Alice"
age=30

# Floating point arithmetic using bc
pi=$(echo "scale=2; 3.14159 / 1" | bc)
echo "Pi (rounded to 2 decimal places): $pi"

# Calculating the area of a circle
radius=5
area=$(echo "scale=2; $pi * $radius * $radius" | bc)
echo "Area of a circle with radius $radius: $area"

# Floating point division
x=10
y=3
result=$(echo "scale=2; $x / $y" | bc)
echo "$x divided by $y is approximately $result"

# More complex floating point calculation
complex_result=$(echo "scale=4; sqrt($x) + $pi" | bc -l)
echo "Square root of $x plus pi: $complex_result"


# Using environment variables
echo "Home directory: $HOME"
# echo "User: $USER"
# echo "Path: $PATH"
# echo "PWD: $PWD"
# echo "Shell: $SHELL"
# echo "Language: $LANG"
# echo "HOSTNAME: $HOSTNAME"
# echo "EDITOR: $EDITOR"
# echo "USER: $USER"

# Command substitution
current_user=$(whoami)
echo "Current user: $current_user"

# Arithmetic operations
result=$((age + 5))
echo "$name will be $result years old in 5 years."

# Additional arithmetic expressions
square=$((age * age))
echo "The square of $name's age is $square."

half_age=$((age / 2))
echo "Half of $name's age is $half_age."

remainder=$((age % 7))
echo "The remainder when $name's age is divided by 7 is $remainder."


# Using expr for arithmetic operations
sum=$(expr $age + 10)
echo "Using expr: $name will be $sum years old in 10 years."

product=$(expr $age \* 2)
echo "Using expr: Twice $name's age is $product."

difference=$(expr $age - 5)
echo "Using expr: Five years ago, $name was $difference years old."

quotient=$(expr $age / 3)
echo "Using expr: One third of $name's age is $quotient."

modulus=$(expr $age % 4)
echo "Using expr: The remainder when $name's age is divided by 4 is $modulus."

# Demonstrating arrays in Bash

# Declare an array
fruits=("apple" "banana" "orange" "grape" "kiwi")

# Print the entire array
echo "All fruits: ${fruits[@]}"

# Print a specific element (0-indexed)
echo "Second fruit: ${fruits[1]}"

# Print the number of elements in the array
echo "Number of fruits: ${#fruits[@]}"

# Add an element to the array
fruits+=("mango")
echo "Updated fruits array: ${fruits[@]}"

# Remove an element from the array (removes the third element, 0-indexed)
unset 'fruits[2]'
echo "Array after removal: ${fruits[@]}"

# Iterate through the array
echo "Listing all fruits:"
for fruit in "${fruits[@]}"; do
    echo "- $fruit"
done

# Array with explicit indices
declare -A car_brands
car_brands[0]="Toyota"
car_brands[1]="Honda"
car_brands[2]="Ford"
car_brands[5]="Tesla"

echo "Car brands:"
for index in "${!car_brands[@]}"; do
    echo "$index: ${car_brands[$index]}"
done

