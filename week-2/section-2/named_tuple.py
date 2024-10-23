from collections import namedtuple

# namedtuple is a factory function for creating tuple subclasses with named fields. 
# It's a convenient way to create simple classes for storing data, similar to a lightweight struct.
# Here's a comprehensive example demonstrating the features and usage of
print("\nnamedtuple:")

# Creating a namedtuple
Point = namedtuple('Point', ['x', 'y'])

# Alternative ways to define fields
# Point = namedtuple('Point', 'x y')
# Point = namedtuple('Point', 'x, y')

# Creating instances
p1 = Point(1, 2)
p2 = Point(x=3, y=4)

print(f"p1: {p1}")
print(f"p2: {p2}")

# Accessing fields
print(f"p1.x: {p1.x}, p1.y: {p1.y}")
print(f"p2.x: {p2[0]}, p2.y: {p2[1]}")  # Can also use index access

# Unpacking
x, y = p1
print(f"Unpacked p1: x={x}, y={y}")

# Using _make() to create instance from iterable
p3 = Point._make([5, 6])
print(f"p3 created with _make(): {p3}")

# Using _asdict() to get OrderedDict
p1_dict = p1._asdict()
print(f"p1 as OrderedDict: {p1_dict}")

# Using _replace() to create a new instance with updated values
p4 = p1._replace(x=10)
print(f"p4 after replacing x in p1: {p4}")

# Demonstrating immutability
try:
    p1.x = 20
except AttributeError as e:
    print(f"Error when trying to modify: {e}")

# Creating a more complex namedtuple
Person = namedtuple('Person', 'name age height', defaults=(0, 0.0))
alice = Person('Alice', 30)
bob = Person('Bob', age=25, height=1.8)

print(f"\nAlice: {alice}")
print(f"Bob: {bob}")

# Using _fields
print(f"Person fields: {Person._fields}")

# Using __annotations__ (Python 3.8+)
print(f"Person annotations: {Person.__annotations__}")

# Creating a subclass of namedtuple
class Employee(namedtuple('Employee', 'name id department')):
    def __str__(self):
        return f"{self.name} (ID: {self.id}) - {self.department}"

emp = Employee('Charlie', 1001, 'IT')
print(f"\nEmployee: {emp}")

# Using _field_defaults
print(f"Person field defaults: {Person._field_defaults}")