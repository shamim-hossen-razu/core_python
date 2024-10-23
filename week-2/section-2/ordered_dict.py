# OrderedDict is a dictionary subclass that remembers the order in which keys were inserted.
# Here's a comprehensive example showcasing OrderedDict methods:

from collections import OrderedDict

print("\nOrderedDict:")

# Creating an OrderedDict
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
print(f"Initial OrderedDict: {od}")

# Adding new items
od['d'] = 4
print(f"After adding 'd': {od}")

# Updating existing items
od['b'] = 22
print(f"After updating 'b': {od}")

# Accessing items
print(f"Value of 'c': {od['c']}")

# Keys, values, and items
print(f"Keys: {list(od.keys())}")
print(f"Values: {list(od.values())}")
print(f"Items: {list(od.items())}")

# Removing items
popped = od.pop('b')
print(f"Popped 'b' (value {popped}): {od}")

# Moving an item to the end
od.move_to_end('a')
print(f"After moving 'a' to end: {od}")

# Moving an item to the beginning
od.move_to_end('d', last=False)
print(f"After moving 'd' to beginning: {od}")

# Reversing the OrderedDict
od_reversed = OrderedDict(reversed(od.items()))
print(f"Reversed OrderedDict: {od_reversed}")

# Equality comparison
od1 = OrderedDict([('a', 1), ('b', 2)])
od2 = OrderedDict([('b', 2), ('a', 1)])
regular_dict = {'a': 1, 'b': 2}

print(f"od1 == od2: {od1 == od2}")  # False, different order
print(f"od1 == regular_dict: {od1 == regular_dict}")  # True, same content

# Copying
od_copy = od.copy()
print(f"Copied OrderedDict: {od_copy}")

# Clearing
od.clear()
print(f"After clearing: {od}")

# Using as a regular dict
od['x'] = 10
od['y'] = 20
print(f"Using as a regular dict: {od}")

# popitem() - default is LIFO
last_item = od.popitem()
print(f"Last item popped: {last_item}, Remaining: {od}")

# popitem(last=False) - FIFO
first_item = od.popitem(last=False)
print(f"First item popped: {first_item}, Remaining: {od}")

# update() method
od.update({'p': 100, 'q': 200})
print(f"After update(): {od}")