from collections import Counter

print("\nCounter:")

# Creating Counters
c1 = Counter(['a', 'b', 'c', 'a', 'b', 'b'])
c2 = Counter({'a': 2, 'b': 3, 'c': 1})
c3 = Counter(a=2, b=3, c=1)

print(f"c1: {c1}")
print(f"c2: {c2}")
print(f"c3: {c3}")

# Counting from a string
text = "abracadabra"
c4 = Counter(text)
print(f"\nCounting characters in '{text}': {c4}")

# Accessing counts
print(f"\nCount of 'a' in c4: {c4['a']}")
print(f"Count of 'z' in c4 (non-existent): {c4['z']}")  # Returns 0 instead of raising an error

# Updating counts
c4.update("aaa")
print(f"c4 after updating with 'aaa': {c4}")

# Most common elements
print(f"\nThree most common elements in c4: {c4.most_common(3)}")

# Elements method
print(f"\nElements in c4: {list(c4.elements())}")

# Set operations
c5 = Counter(a=3, b=1, c=2)
c6 = Counter(a=1, b=2, d=3)

print(f"\nc5: {c5}")
print(f"c6: {c6}")

print(f"c5 + c6: {c5 + c6}")  # Addition
print(f"c5 - c6: {c5 - c6}")  # Subtraction (keeping only positive counts)
print(f"c5 & c6: {c5 & c6}")  # Intersection (minimum of each element count)
print(f"c5 | c6: {c5 | c6}")  # Union (maximum of each element count)

# Unary operations
print(f"\n+c5: {+c5}")  # Keeping only positive counts
print(f"-c5: {-c5}")  # Inverting counts

# Subtracting counts
c5.subtract(c6)
print(f"\nc5 after subtracting c6: {c5}")

# Total count
print(f"\nTotal count in c4: {sum(c4.values())}")

# Clearing a counter
c6.clear()
print(f"\nc6 after clearing: {c6}")

# Using with strings and lists
words = ['red', 'blue', 'red', 'green', 'blue', 'blue']
c7 = Counter(words)
print(f"\nWord counts: {c7}")

# Finding the most common word
most_common_word = c7.most_common(1)[0][0]
print(f"Most common word: {most_common_word}")

# Counting words in a sentence
sentence = "how much wood would a woodchuck chuck if a woodchuck could chuck wood"
word_counts = Counter(sentence.split())
print(f"\nWord counts in sentence: {word_counts}")

# Finding unique elements
unique_elements = list(Counter(words).keys())
print(f"\nUnique words: {unique_elements}")

| Feature           | Tuple                       | Named Tuple                     |
|-------------------|-----------------------------|---------------------------------|
| Definition        | Built-in type               | Factory function in collections |
| Syntax            | (item1, item2, ...)         | namedtuple('Name', ['field1', 'field2', ...]) |
| Access by Index   | Yes                         | Yes                             |
| Access by Name    | No                          | Yes                             |
| Immutability      | Yes                         | Yes                             |
| Memory Efficiency | Very efficient              | Slightly less efficient than tuple |
| Readability       | Less readable for complex data | More readable, self-documenting |
| Default Values    | No                          | Yes (in Python 3.7+)            |
| Inheritance       | Not typically subclassed    | Can be subclassed easily        |

Example Usage: