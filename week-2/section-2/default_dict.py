from collections import defaultdict

print("\ndefaultdict:")

# Creating defaultdicts with different default_factory functions
dd_list = defaultdict(list)
dd_int = defaultdict(int)
dd_str = defaultdict(str)
dd_set = defaultdict(set)

# Using lambda for custom default values
dd_custom = defaultdict(lambda: "Not found")

# Demonstrating list as default_factory
print("\n1. defaultdict(list):")
fruits = [("apple", "red"), ("banana", "yellow"), ("apple", "green")]
fruit_colors = defaultdict(list)

for fruit, color in fruits:
    fruit_colors[fruit].append(color)

print(f"Fruit colors: {dict(fruit_colors)}")
print(f"Accessing non-existent key 'orange': {fruit_colors['orange']}")

# Demonstrating int as default_factory (useful for counting)
print("\n2. defaultdict(int):")
word_count = defaultdict(int)
sentence = "the quick brown fox jumps over the lazy dog"
for word in sentence.split():
    word_count[word] += 1

print(f"Word counts: {word_count}")
print(f"Count of non-existent word 'cat': {word_count['cat']}")

# Demonstrating str as default_factory
print("\n3. defaultdict(str):")
name_prefix = defaultdict(str)
name_prefix.update({"John": "Mr.", "Jane": "Ms."})
print(f"John's prefix: {name_prefix['John']}")
print(f"Unknown name's prefix: {name_prefix['Alice']}")

# Demonstrating set as default_factory
print("\n4. defaultdict(set):")
fruit_colors_set = defaultdict(set)
for fruit, color in fruits:
    fruit_colors_set[fruit].add(color)

print(f"Fruit colors (unique): {dict(fruit_colors_set)}")

# Demonstrating custom default_factory
print("\n5. defaultdict with custom default:")
stock_status = defaultdict(lambda: "Out of stock")
stock_status.update({"apple": "In stock", "banana": "Low stock"})
print(f"Apple status: {stock_status['apple']}")
print(f"Orange status: {stock_status['orange']}")

# Other dict operations work normally
print("\nOther dict operations:")
dd = defaultdict(int, {'a': 1, 'b': 2})
print(f"Initial dd: {dict(dd)}")
dd['c'] = 3
print(f"After adding 'c': {dict(dd)}")
del dd['b']
print(f"After deleting 'b': {dict(dd)}")
print(f"Keys: {list(dd.keys())}")
print(f"Values: {list(dd.values())}")
print(f"Items: {list(dd.items())}")

# Copying a defaultdict
dd_copy = dd.copy()
print(f"Copied defaultdict: {dict(dd_copy)}")
print(f"Is copy also a defaultdict? {isinstance(dd_copy, defaultdict)}")
print(f"Default factory of copy: {dd_copy.default_factory}")