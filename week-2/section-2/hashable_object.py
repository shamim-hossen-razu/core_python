# Hashable objects
print("Hashable objects:")
print(f"Hash of int 42: {hash(42)}")
print(f"Hash of float 3.14: {hash(3.14)}")
print(f"Hash of string 'hello': {hash('hello')}")
print(f"Hash of tuple (1, 2, 3): {hash((1, 2, 3))}")
a = 42
print('TEST', a.__hash__())
print('TEST', a.__eq__(43))

# Non-hashable objects
print("\nNon-hashable objects:")
try:
    print(f"Hash of list [1, 2, 3]: {hash([1, 2, 3])}")
except TypeError as e:
    print(f"Error: {e}")

try:
    print(f"Hash of dict {{1: 'a', 2: 'b'}}: {hash({1: 'a', 2: 'b'})}")
except TypeError as e:
    print(f"Error: {e}")

# Custom hashable object
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __hash__(self):
        return hash((self.x, self.y))
    
    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x and self.y == other.y

p1 = Point(1, 2)
p2 = Point(1, 2)
print(f"\nHash of Point(1, 2): {hash(p1)}")
print(f"Are p1 and p2 equal? {p1 == p2}")
print(f"Do p1 and p2 have the same hash? {hash(p1) == hash(p2)}")

# Using hashable objects as dictionary keys
d = {p1: 'first point'}
print(f"\nDictionary with Point as key: {d}")
print(f"Value for p2 in dictionary: {d.get(p2)}")

# Example 1: Default behavior (hashable)
class DefaultClass:
    pass

obj1 = DefaultClass()
print(f"Hash of DefaultClass: {hash(obj1)}")  # This works

# Example 2: Defining __eq__ without __hash__ (unhashable)
class UnhashableClass:
    def __eq__(self, other):
        return isinstance(other, UnhashableClass)

obj2 = UnhashableClass()
try:
    print(f"Hash of UnhashableClass: {hash(obj2)}")
except TypeError as e:
    print(f"Error: {e}")  # This will print an error

# Example 3: Explicitly making a class unhashable
class ExplicitlyUnhashable:
    __hash__ = None

obj3 = ExplicitlyUnhashable()
try:
    print(f"Hash of ExplicitlyUnhashable: {hash(obj3)}")
except TypeError as e:
    print(f"Error: {e}")  # This will print an error

# Example 4: Proper implementation of a hashable class
class HashableClass:
    def __init__(self, value):
        self.value = value
    
    def __eq__(self, other):
        return isinstance(other, HashableClass) and self.value == other.value
    
    def __hash__(self):
        return hash(self.value)

obj4 = HashableClass(42)
print(f"Hash of HashableClass: {hash(obj4)}")  # This works