# Python provides several built-in iterators and functions that return iterators. Here are some of the most commonly used built-in iterators and iterator-producing functions:


# 1. iter() Function
# The iter() function can be used to obtain an iterator from any iterable (like lists, tuples, strings, etc.).

my_list = [1, 2, 3]
list_iterator = iter(my_list)
print(next(list_iterator))  # Output: 1

# 2. range() Function
# The range() function returns an immutable sequence of numbers and can be used as an iterator.

for i in range(5):
    print(i)  # Output: 0, 1, 2, 3, 4


# 3. File Objects
# - File objects in Python are iterators that yield lines from the file one at a time.
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())  # Prints each line from the file


# 4. enumerate() Function
# - The `enumerate()` function takes an iterable and returns an iterator that produces pairs of an 
# index and the corresponding item from the iterable.

with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())  # Prints each line from the file


### 5. **`zip()` Function**
# - The `zip()` function takes multiple iterables and returns an iterator that aggregates elements from each iterable.

names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(name, age)


# 6. map() Function
# - The `map()` function applies a function to every item of an iterable and returns an iterator.

squared = map(lambda x: x ** 2, range(5))
for num in squared:
    print(num)  # Output: 0, 1, 4, 9, 16


# 7. filter() Function
# - The `filter()` function constructs an iterator from elements of an iterable for which a function returns true.
even_numbers = filter(lambda x: x % 2 == 0, range(10))
for num in even_numbers:
    print(num)  # Output: 0, 2, 4, 6, 8
    