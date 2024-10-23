# Iterators in Python

# Creating an iterator
class MyIterator:
    def __init__(self, data):
        self.index = 0
        self.data = data

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        result = self.data[self.index]
        self.index += 1
        return result

# Using the iterator
my_data = [1, 2, 3, 4, 5]
my_iter = MyIterator(my_data)

# for item in my_iter.__iter__():
#     print('itenm', item)
# print('TEST', my_iter.__next__())
# print('TEST', my_iter.__next__())
# print('TEST', my_iter.__next__())
# print('TEST', my_iter.__next__())
# print('TEST', my_iter.__next__())
# print('TEST', my_iter.__next__())
print(my_iter.__iter__())

for item in my_iter:
    print(item)

# Built-in iterators
# Iterating over a list
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

# what happens behind the scene
# fruits = ['apple', 'banana', 'cherry']
# iterator = iter(fruits)

# while True:
#     try:
#         fruit = next(iterator)
#         print(fruit)
#     except StopIteration:
#         break

# Iterating over a string
for char in "hello":
    print(char)

# Iterating over a dictionary
person = {"name": "Alice", "age": 30, "city": "New York"}
for key in person:
    print(f"{key}: {person[key]}")

# Iterating over a set
colors = {'red', 'green', 'blue'}
for color in colors:
    print(color)

# Iterating over a tuple
numbers = (1, 2, 3, 4, 5)
for number in numbers:
    print(number)
