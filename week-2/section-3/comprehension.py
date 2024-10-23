# List comprehension with conditional
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in numbers if num % 2 == 0]
print("Even numbers:", even_numbers)

# Set comprehension with conditional
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
fruits_starting_with_a = {fruit for fruit in fruits if fruit.startswith('a')}
print("Fruits starting with 'a':", fruits_starting_with_a)

# Dictionary comprehension with conditional
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 90},
    {"name": "Charlie", "grade": 78},
    {"name": "David", "grade": 92},
    {"name": "Eve", "grade": 88}
]
high_achievers = {student["name"]: student["grade"] for student in students if student["grade"] >= 90}
print("High achievers:", high_achievers)
