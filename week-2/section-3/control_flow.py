# Comparison Operators
print("Comparison Operators:")
x, y = 5, 10
print(f"x = {x}, y = {y}")
print(f"x == y: {x == y}")
print(f"x != y: {x != y}")
print(f"x < y: {x < y}")
print(f"x > y: {x > y}")
print(f"x <= y: {x <= y}")
print(f"x >= y: {x >= y}")

# Logical Operators
print("\nLogical Operators:")
a, b = True, False
print(f"a = {a}, b = {b}")
print(f"a and b: {a and b}")
print(f"a or b: {a or b}")
print(f"not a: {not a}")

# Conditional Statements
print("\nConditional Statements:")
age = 18
if age < 18:
    print("You are a minor.")
elif age == 18:
    print("You just became an adult!")
else:
    print("You are an adult.")

# Ternary Operator
is_adult = "Adult" if age >= 18 else "Minor"
print(f"Status: {is_adult}")

# Looping
print("\nLooping:")

# For loop
print("For loop:")
for i in range(5):
    print(i, end=" ")
print()

# While loop
print("\nWhile loop:")
count = 0
while count < 5:
    print(count, end=" ")
    count += 1
print()

# Loop with break and continue
print("\nLoop with break and continue:")
for i in range(10):
    if i == 3:
        continue
    if i == 7:
        break
    print(i, end=" ")
print()

# List comprehension
print("\nList comprehension:")
squares = [x**2 for x in range(5)]
print(f"Squares: {squares}")

# Nested loops
print("\nNested loops:")
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})", end=" ")
    print()

# Iterating over a dictionary
print("\nIterating over a dictionary:")
person = {"name": "Alice", "age": 30, "city": "New York"}
for key, value in person.items():
    print(f"{key}: {value}")

# Enumerate
print("\nEnumerate:")
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Zip
print("\nZip:")
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

