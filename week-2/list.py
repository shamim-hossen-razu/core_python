# Comprehensive Guide to Lists in Python

# 1. Creating Lists
print("1. Creating Lists:")
empty_list = []
numbers = [1, 2, 3, 4, 5]
mixed_list = [1, "two", 3.0, [4, 5]]
list_from_range = list(range(5))
list_from_string = list("Python")

print(f"Empty list: {empty_list}")
print(f"List of numbers: {numbers}")
print(f"Mixed list: {mixed_list}")
print(f"List from range: {list_from_range}")
print(f"List from string: {list_from_string}")

# 2. Accessing List Elements
print("\n2. Accessing List Elements:")
fruits = ["apple", "banana", "cherry", "date"]
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")
print(f"Slicing (1:3): {fruits[1:3]}")
print(f"Every second fruit: {fruits[::2]}")
print(f"Reversed list: {fruits[::-1]}")

# 3. Modifying Lists
print("\n3. Modifying Lists:")
fruits[1] = "blueberry"
fruits.append("elderberry")
fruits.insert(2, "fig")
fruits.extend(["grape", "honeydew"])
print(f"Modified fruits list: {fruits}")

# 4. Removing Elements
print("\n4. Removing Elements:")
removed_fruit = fruits.pop()
print(f"Removed fruit: {removed_fruit}")
fruits.remove("fig")
del fruits[0]
fruits.clear()  # Removes all elements
print(f"List after removals and clear: {fruits}")

# 5. List Operations
print("\n5. List Operations:")
numbers = [1, 2, 3]
doubled = numbers * 2
combined = numbers + [4, 5, 6]
print(f"Doubled list: {doubled}")
print(f"Combined list: {combined}")
print(f"Length of combined list: {len(combined)}")

# 6. List Methods
print("\n6. List Methods:")
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
numbers.sort()
print(f"Sorted list: {numbers}")
numbers.reverse()
print(f"Reversed list: {numbers}")
print(f"Count of 5: {numbers.count(5)}")
print(f"Index of 4: {numbers.index(4)}")
numbers_copy = numbers.copy()
print(f"Copied list: {numbers_copy}")

# 7. List Comprehensions
print("\n7. List Comprehensions:")
squares = [x**2 for x in range(10)]
even_squares = [x**2 for x in range(10) if x % 2 == 0]
matrix = [[i+j for j in range(3)] for i in range(3)]
print(f"Squares: {squares}")
print(f"Even squares: {even_squares}")
print(f"Matrix: {matrix}")

# 8. Nested Lists
print("\n8. Nested Lists:")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"Matrix: {matrix}")
print(f"Element at row 1, column 2: {matrix[1][2]}")
flattened = [num for row in matrix for num in row]
print(f"Flattened matrix: {flattened}")

# 9. List Copying
print("\n9. List Copying:")
import copy
original = [1, [2, 3], 4]
shallow_copy = original.copy()
deep_copy = copy.deepcopy(original)
original[1][0] = 'X'
print(f"Original: {original}, Shallow copy: {shallow_copy}, Deep copy: {deep_copy}")

# 10. List as Stack and Queue
print("\n10. List as Stack and Queue:")
stack = [1, 2, 3]
stack.append(4)
print(f"Stack: {stack}")
print(f"Popped: {stack.pop()}")

from collections import deque
queue = deque(["a", "b", "c"])
queue.append("d")
print(f"Queue: {queue}")
print(f"Dequeued: {queue.popleft()}")

# 11. List Unpacking
print("\n11. List Unpacking:")
a, b, c = [1, 2, 3]
print(f"Unpacked values: a={a}, b={b}, c={c}")
first, *rest, last = [1, 2, 3, 4, 5]
print(f"Extended unpacking: first={first}, rest={rest}, last={last}")

# 12. List Membership and Comparison
print("\n12. List Membership and Comparison:")
fruits = ["apple", "banana", "cherry"]
print(f"Is 'apple' in fruits? {'apple' in fruits}")
print(f"Is 'mango' not in fruits? {'mango' not in fruits}")
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(f"Are list1 and list2 equal? {list1 == list2}")
print(f"Are list1 and list2 the same object? {list1 is list2}")

# 13. List Iteration
print("\n13. List Iteration:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# 14. List Performance Considerations
print("\n14. List Performance Considerations:")
print("- Appending to the end of a list is generally O(1)")
print("- Inserting or deleting from the beginning is O(n)")
print("- Accessing by index is O(1)")
print("- Searching for an element is O(n)")
print("- Slicing is O(k) where k is the size of the slice")

# 15. Advanced List Techniques
print("\n15. Advanced List Techniques:")
from itertools import zip_longest
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c', 'd']
zipped = list(zip_longest(list1, list2, fillvalue=None))
print(f"Zipped lists: {zipped}")

# List filtering
odd_numbers = list(filter(lambda x: x % 2 != 0, range(10)))
print(f"Odd numbers: {odd_numbers}")

# List mapping
squared_numbers = list(map(lambda x: x**2, range(5)))
print(f"Squared numbers: {squared_numbers}")

# Sorting with custom key
words = ['apple', 'banana', 'cherry', 'date']
sorted_words = sorted(words, key=len)
print(f"Words sorted by length: {sorted_words}")

# This comprehensive guide covers most aspects of working with lists in Python,
# from basic operations to advanced techniques.

