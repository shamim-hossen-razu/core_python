# Comprehensive Guide to Tuples in Python

# 1. Creating Tuples
print("1. Creating Tuples:")
empty_tuple = ()
single_item_tuple = (1,)  # Note the comma
mixed_tuple = (1, "two", 3.0, True)
nested_tuple = (1, (2, 3), [4, 5])
tuple_from_list = tuple([1, 2, 3])
tuple_unpacking = x, y, z = (1, 2, 3)

print(f"Empty tuple: {empty_tuple}")
print(f"Single item tuple: {single_item_tuple}")
print(f"Mixed tuple: {mixed_tuple}")
print(f"Nested tuple: {nested_tuple}")
print(f"Tuple from list: {tuple_from_list}")
print(f"Tuple unpacking: x={x}, y={y}, z={z}")

# 2. Accessing Tuple Elements
print("\n2. Accessing Tuple Elements:")
my_tuple = (1, 2, 3, 4, 5)
print(f"First element: {my_tuple[0]}")
print(f"Last element: {my_tuple[-1]}")
print(f"Slicing (1:3): {my_tuple[1:3]}")
print(f"Reverse slicing (3:1:-1): {my_tuple[3:1:-1]}")

# 3. Tuple Operations
print("\n3. Tuple Operations:")
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated = tuple1 + tuple2
repeated = tuple1 * 3
print(f"Concatenation: {concatenated}")
print(f"Repetition: {repeated}")
print(f"Length of tuple: {len(tuple1)}")

# 4. Tuple Methods
print("\n4. Tuple Methods:")
sample_tuple = (1, 2, 2, 3, 4, 2)
print(f"Count of 2: {sample_tuple.count(2)}")
print(f"Index of 3: {sample_tuple.index(3)}")
print(f"Index of 2 starting from position 2: {sample_tuple.index(2, 2)}")

# 5. Tuple Immutability
print("\n5. Tuple Immutability:")
# my_tuple[0] = 10  # This would raise a TypeError
print("Tuples are immutable, so we can't modify their elements.")
print("However, if a tuple contains mutable objects, those objects can be changed:")
mutable_in_tuple = ([1, 2], [3, 4])
mutable_in_tuple[0].append(3)
print(f"Tuple after modifying mutable object: {mutable_in_tuple}")

# 6. Tuple Comparison
print("\n6. Tuple Comparison:")
tuple1 = (1, 2, 3)
tuple2 = (1, 2, 4)
tuple3 = (1, 2, 3, 4)
print(f"tuple1 == tuple2: {tuple1 == tuple2}")
print(f"tuple1 < tuple2: {tuple1 < tuple2}")
print(f"tuple1 < tuple3: {tuple1 < tuple3}")

# 7. Tuple as Return Values
print("\n7. Tuple as Return Values:")
def min_max(numbers):
    return min(numbers), max(numbers)

result = min_max([1, 5, 3, 9, 2])
print(f"Min and Max: {result}")

# 8. Tuple Comprehension (Generator Expression)
print("\n8. Tuple Comprehension:")
tuple_comp = tuple(x**2 for x in range(5))
print(f"Tuple comprehension result: {tuple_comp}")

# 9. Named Tuples
print("\n9. Named Tuples:")
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(f"Named tuple: {p}")
print(f"Accessing named tuple: p.x = {p.x}, p.y = {p.y}")
print(f"Converting named tuple to dict: {p._asdict()}")

# 10. Tuple vs List
print("\n10. Tuple vs List:")
print("- Tuples are immutable, lists are mutable")
print("- Tuples are typically faster than lists")
print("- Tuples can be used as dictionary keys, lists cannot")
print("- Tuples are used for heterogeneous data, lists for homogeneous data")
import sys
list_ex = [1, 2, 3, 4, 5]
tuple_ex = (1, 2, 3, 4, 5)
print(f"Size of list: {sys.getsizeof(list_ex)} bytes")
print(f"Size of tuple: {sys.getsizeof(tuple_ex)} bytes")

# 11. Tuple Packing and Unpacking
print("\n11. Tuple Packing and Unpacking:")
packed = 1, 2, 3  # Packing
a, b, c = packed  # Unpacking
print(f"Packed: {packed}")
print(f"Unpacked: a={a}, b={b}, c={c}")
# Extended unpacking
a, *b, c = (1, 2, 3, 4, 5)
print(f"Extended unpacking: a={a}, b={b}, c={c}")

# 12. Using Tuples in Functions
print("\n12. Using Tuples in Functions:")
def sum_and_product(a, b):
    return (a+b, a*b)

result = sum_and_product(3, 4)
print(f"Sum and product: {result}")

# Function with arbitrary number of arguments
def print_args(*args):
    print(f"Arguments received: {args}")

print_args(1, 2, 3, 'a', 'b')

# 13. Tuple as a Sequence Type
print("\n13. Tuple as a Sequence Type:")
my_tuple = (1, 2, 3, 4, 5)
print(f"Length: {len(my_tuple)}")
print(f"Minimum: {min(my_tuple)}")
print(f"Maximum: {max(my_tuple)}")
print(f"Sum: {sum(my_tuple)}")
print(f"Sorted tuple: {tuple(sorted(my_tuple, reverse=True))}")

# 14. Nested Tuple Unpacking
print("\n14. Nested Tuple Unpacking:")
nested = ((1, 2), (3, 4))
(a, b), (c, d) = nested
print(f"Nested unpacking: a={a}, b={b}, c={c}, d={d}")

# 15. Tuple with Different Data Types
print("\n15. Tuple with Different Data Types:")
mixed = (1, "hello", [1, 2, 3], {"a": 1, "b": 2})
print(f"Mixed tuple: {mixed}")
print(f"Accessing list inside tuple: {mixed[2][1]}")
print(f"Accessing dict inside tuple: {mixed[3]['a']}")

# 16. Tuple Conversion
print("\n16. Tuple Conversion:")
list_to_tuple = tuple([1, 2, 3])
set_to_tuple = tuple({1, 2, 3})
string_to_tuple = tuple("hello")
print(f"List to tuple: {list_to_tuple}")
print(f"Set to tuple: {set_to_tuple}")
print(f"String to tuple: {string_to_tuple}")

# 17. Tuple in Control Flow
print("\n17. Tuple in Control Flow:")
for item in (1, 2, 3):
    print(item)

# 18. Tuple as Dictionary Key
print("\n18. Tuple as Dictionary Key:")
coord_dict = {(0, 0): 'origin', (1, 0): 'right', (0, 1): 'up'}
print(f"Dictionary with tuple keys: {coord_dict}")

# 19. Tuple Performance
print("\n19. Tuple Performance:")
import timeit
list_time = timeit.timeit(stmt="[1, 2, 3, 4, 5]", number=1000000)
tuple_time = timeit.timeit(stmt="(1, 2, 3, 4, 5)", number=1000000)
print(f"Time to create list 1,000,000 times: {list_time}")
print(f"Time to create tuple 1,000,000 times: {tuple_time}")

# 20. Tuple Hashing
print("\n20. Tuple Hashing:")
print(f"Hash of (1, 2, 3): {hash((1, 2, 3))}")
# print(f"Hash of [1, 2, 3]: {hash([1, 2, 3])}")  # This would raise a TypeError

# This comprehensive guide covers all aspects of working with tuples in Python,
# from basic operations to advanced techniques and performance considerations.

