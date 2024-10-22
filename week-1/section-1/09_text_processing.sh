#!/bin/bash

# Using cut to extract fields
echo "John,Doe,30" | cut -d',' -f2
# Output: Doe

# Using sed for text substitution
echo "Hello, World!" | sed 's/World/Bash/'
# Output: Hello, Bash!

# Using awk for field processing
echo "John Doe 30" | awk '{print $2, $1}'
# Output: Doe John

# Using grep with regular expressions
echo "The quick brown fox" | grep -E '\b\w{5}\b'
# Output: quick brown


# cut -d',' -f2 data.csv
# sed 's/World/Bash/' file.txt
# awk '{print $2, $1}' names.txt
# grep -E '\b\w{5}\b' document.txt

# cat file.txt | sed 's/World/Bash/'
# ls -l | awk '{print $9}'