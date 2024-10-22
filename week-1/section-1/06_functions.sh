#!/bin/bash

# Defining a function
greet() {
    echo "Hello, $1!"
}

# Calling the function
greet "Alice"

# Function with return value
add() {
    local result=$(($1 + $2))
    echo $result
}

# Using the function's return value
sum=$(add 5 3)
echo "5 + 3 = $sum"

# return value
add() {
    local result=$(($1 + $2))
    return $result
}

# Using the function's return value
add 5 3
sum=$?
echo "5 + 3 = $sum"

# setting a global variable
result=0

add() {
    result=$(($1 + $2))
}

# Using the function
add 5 3
echo "5 + 3 = $result"


# Function with multiple parameters
calculate() {
    case $2 in
        "+") echo $(($1 + $3));;
        "-") echo $(($1 - $3));;
        "*") echo $(($1 * $3));;
        "/") echo $(($1 / $3));;
        *) echo "Invalid operator";;
    esac
}

# Using the calculate function
result=$(calculate 10 "+" 5)
echo "10 + 5 = $result"

result=$(calculate 20 "*" 3)
echo "20 * 3 = $result"

# Function with default parameter
greet_user() {
    local name=${1:-"Guest"}
    echo "Welcome, $name!"
}

greet_user
greet_user "John"

# Recursive function
factorial() {
    if [ $1 -eq 0 ] || [ $1 -eq 1 ]; then
        echo 1
    else
        local temp=$(factorial $(($1 - 1)))
        echo $(($1 * temp))
    fi
}

# Using the recursive function
result=$(factorial 5)
echo "Factorial of 5 is $result"

# Function that uses command substitution
get_files() {
    echo $(ls $1)
}

files=$(get_files "/tmp")
echo "Files in /tmp: $files"
