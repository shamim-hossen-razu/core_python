# Comprehensive Guide to Python Strings

# 1. String Creation
simple_string = "Hello, World!"  # Using double quotes
another_string = 'Python is great'  # Using single quotes
multi_line_string = """This is a
multi-line string."""  # Using triple quotes for multi-line strings

print("String Creation:")
print(simple_string)
print(another_string)
print(multi_line_string)

# 2. String Indexing and Slicing
print("\nString Indexing and Slicing:")
# Indexing: accessing individual characters
print("First character:", simple_string[0])  # Prints 'H'
print("Last character:", simple_string[-1])  # Prints '!'

# Slicing: extracting a portion of the string
print("Slicing (3:8):", simple_string[3:8])  # Prints 'lo, W'
print("Slicing with step (::2):", simple_string[::2])  # Prints 'Hlo ol!' (every second character)
print("Reverse string:", simple_string[::-1])  # Prints '!dlroW ,olleH'

# 3. String Manipulation
print("\nString Manipulation:")
# Concatenation
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print("Concatenated string:", full_name)

# Repetition
repeated_string = "Echo " * 3
print("Repeated string:", repeated_string)

# 4. String Methods
print("\nString Methods:")
sample_string = "  Python is Awesome!  "

# Case manipulation
print("Lowercase:", sample_string.lower())
print("Uppercase:", sample_string.upper())
print("Title case:", sample_string.title())
print("Swapcase:", sample_string.swapcase())

# Whitespace removal
print("Strip:", sample_string.strip())
print("Left Strip:", sample_string.lstrip())
print("Right Strip:", sample_string.rstrip())

# Searching and replacing
print("Replace:", sample_string.replace("Awesome", "Amazing"))
print("Count 'is':", sample_string.count('is'))
print("Find 'is':", sample_string.find('is'))
print("Right find 'is':", sample_string.rfind('is'))

# Splitting and joining
words = sample_string.split()
print("Split:", words)
print("Join:", "-".join(words))

# Checking string properties
print("Is alphanumeric:", "Python3".isalnum())
print("Is alphabetic:", "Python".isalpha())
print("Is digit:", "12345".isdigit())
print("Starts with 'Py':", sample_string.strip().startswith("Py"))
print("Ends with '!':", sample_string.strip().endswith("!"))

# 5. String Formatting
print("\nString Formatting:")
name = "Alice"
age = 30

# Using f-strings (Python 3.6+)
formatted_string = f"{name} is {age} years old."
print("F-string:", formatted_string)

# Using .format() method
formatted_string = "{} is {} years old.".format(name, age)
print("Format method:", formatted_string)

# Using % operator (older style)
formatted_string = "%s is %d years old." % (name, age)
print("% operator:", formatted_string)

# 6. String Iteration
print("\nString Iteration:")
for char in "Python":
    print(char, end=" ")
print()  # New line

# 7. String Comparison
print("\nString Comparison:")
string1 = "apple"
string2 = "banana"
print("apple == banana:", string1 == string2)
print("apple < banana:", string1 < string2)  # Lexicographical comparison

# 8. Escape Characters
print("\nEscape Characters:")
print("New line:\nSecond line")
print("Tab:\tIndented")
print("Backslash: \\")
print("Quote: \"")

# 9. Raw Strings
print("\nRaw Strings:")
raw_string = r"C:\Users\John\Documents"
print("Raw string:", raw_string)

# 10. String Encoding and Decoding
print("\nString Encoding and Decoding:")
encoded = "Python".encode('utf-8')
print("Encoded:", encoded)
decoded = encoded.decode('utf-8')
print("Decoded:", decoded)

# 11. Real-life String Problem: Parsing a CSV-like string
print("\nReal-life String Problem: Parsing a CSV-like string")
csv_string = "John,Doe,30,New York"
parsed_data = csv_string.split(',')
print("Parsed CSV:", parsed_data)

# 12. Advanced String Methods
print("\nAdvanced String Methods:")
text = "Python is a versatile programming language."
print("Center:", text.center(50, '-'))
print("Partition:", text.partition('versatile'))
print("Translate:", text.translate(str.maketrans('aeiou', '12345')))

# 13. String Immutability
print("\nString Immutability:")
s = "Hello"
# s[0] = 'h'  # This would raise an error
s = 'h' + s[1:]  # This creates a new string
print("Modified string:", s)

# 14. String Interpolation (Python 3.6+)
print("\nString Interpolation:")
x = 10
y = 20
print(f"The sum of {x} and {y} is {x + y}")

# 15. Multi-line String as Documentation
def example_function():
    """
    This is a multi-line string used as a docstring.
    It can span multiple lines and is used to document
    functions, classes, and modules.
    """
    pass

print("\nDocstring:")
print(example_function.__doc__)


