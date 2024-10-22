# Comprehensive Guide to Python Dictionaries

# 1. Creating Dictionaries
print("1. Creating Dictionaries:")
empty_dict = {}
simple_dict = {"name": "John", "age": 30, "city": "New York"}
dict_constructor = dict(name="Alice", age=25, city="London")
dict_from_list = dict([("fruit", "apple"), ("vegetable", "carrot")])

print(f"Empty dictionary: {empty_dict}")
print(f"Simple dictionary: {simple_dict}")
print(f"Dictionary from constructor: {dict_constructor}")
print(f"Dictionary from list of tuples: {dict_from_list}")

# 2. Accessing Dictionary Elements
print("\n2. Accessing Dictionary Elements:")
person = {"name": "Bob", "age": 35, "job": "Engineer"}
print(f"Name: {person['name']}")
print(f"Age: {person.get('age')}")
print(f"Salary (with default): {person.get('salary', 'Not specified')}")

# 3. Modifying Dictionaries
print("\n3. Modifying Dictionaries:")
person["age"] = 36
person["salary"] = 75000
person.update({"city": "San Francisco", "department": "IT"})
print(f"Updated person: {person}")

# 4. Removing Items
print("\n4. Removing Items:")
removed_job = person.pop("job")
print(f"Removed job: {removed_job}")
last_item = person.popitem()
print(f"Last removed item: {last_item}")
del person["age"]
print(f"After deletions: {person}")

# 5. Dictionary Methods
print("\n5. Dictionary Methods:")
keys = person.keys()
values = person.values()
items = person.items()
print(f"Keys: {keys}")
print(f"Values: {values}")
print(f"Items: {items}")

# 6. Dictionary Comprehension
print("\n6. Dictionary Comprehension:")
squares = {x: x**2 for x in range(6)}
print(f"Squares: {squares}")

# 7. Nested Dictionaries
print("\n7. Nested Dictionaries:")
nested_dict = {
    "person1": {"name": "Alice", "age": 30},
    "person2": {"name": "Bob", "age": 35}
}
print(f"Nested dictionary: {nested_dict}")
print(f"Person1's age: {nested_dict['person1']['age']}")

# 8. Dictionary Membership Test
print("\n8. Dictionary Membership Test:")
print(f"Is 'name' in person? {'name' in person}")
print(f"Is 'gender' not in person? {'gender' not in person}")

# 9. Iterating Through Dictionaries
print("\n9. Iterating Through Dictionaries:")
for key in person:
    print(f"{key}: {person[key]}")

for key, value in person.items():
    print(f"{key}: {value}")

# 10. Copying Dictionaries
print("\n10. Copying Dictionaries:")
import copy
shallow_copy = person.copy()
deep_copy = copy.deepcopy(nested_dict)
print(f"Shallow copy: {shallow_copy}")
print(f"Deep copy: {deep_copy}")

# 11. Dictionary Views
print("\n11. Dictionary Views:")
keys_view = person.keys()
print(f"Keys view: {keys_view}")
person["new_key"] = "new_value"
print(f"Updated keys view: {keys_view}")

# 12. Dictionary Unpacking
print("\n12. Dictionary Unpacking:")
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
combined = {**dict1, **dict2}
print(f"Combined dictionary: {combined}")

# 13. Dictionary from Zip
print("\n13. Dictionary from Zip:")
keys = ["name", "age", "city"]
values = ["Charlie", 40, "Chicago"]
zipped_dict = dict(zip(keys, values))
print(f"Zipped dictionary: {zipped_dict}")

# 14. Dictionary Sorting
print("\n14. Dictionary Sorting:")
unsorted = {"b": 2, "c": 3, "a": 1}
sorted_by_key = dict(sorted(unsorted.items()))
sorted_by_value = dict(sorted(unsorted.items(), key=lambda item: item[1]))
print(f"Sorted by key: {sorted_by_key}")
print(f"Sorted by value: {sorted_by_value}")

# 15. Dictionary Performance
print("\n15. Dictionary Performance:")
print("- Average time complexity for get/set/delete: O(1)")
print("- Worst-case time complexity (rare): O(n)")
print("- Space complexity: O(n)")

# 16. Advanced Dictionary Techniques
print("\n16. Advanced Dictionary Techniques:")
from collections import defaultdict, OrderedDict, Counter

# defaultdict
default_dict = defaultdict(int)
words = ["apple", "banana", "apple", "cherry", "banana", "date"]
for word in words:
    default_dict[word] += 1
print(f"Word count with defaultdict: {dict(default_dict)}")

# OrderedDict
ordered_dict = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(f"Ordered dictionary: {ordered_dict}")

# Counter
counter = Counter(words)
print(f"Counter: {counter}")
print(f"Most common 2 items: {counter.most_common(2)}")

# This comprehensive guide covers all major aspects of working with dictionaries in Python,
# from basic operations to advanced techniques and performance considerations.
