# All about strings in Python

# Creating strings
single_quoted = 'Hello, World!'
double_quoted = "Hello, World!"
triple_quoted = '''This is a
multi-line string'''

print("Creating strings:")
print(single_quoted)
print(double_quoted)
print(triple_quoted)

# String concatenation
str1 = "Hello"
str2 = "World"
concatenated = str1 + " " + str2
print("\nConcatenation:", concatenated)

# String repetition
repeated = "Echo " * 3
print("Repetition:", repeated)

# String indexing and slicing
sample = "Python"
print("\nIndexing and Slicing:")
print("First character:", sample[0])
print("Last character:", sample[-1])
print("Slicing (1:4):", sample[1:4])
print("Reverse:", sample[::-1])

# String methods
text = "  Python is awesome!  "
print("\nString methods:")
print("Upper:", text.upper())
print("Lower:", text.lower())
print("Capitalize:", text.capitalize())
print("Title:", text.title())
print("Strip:", text.strip())
print("Replace:", text.replace("awesome", "amazing"))
print("Split:", text.split())
print("Join:", "-".join(["Python", "is", "fun"]))

# String formatting
name = "Alice"
age = 30
print("\nString formatting:")
print("Using %: My name is %s and I'm %d years old." % (name, age))
print("Using format(): My name is {} and I'm {} years old.".format(name, age))
print(f"Using f-strings: My name is {name} and I'm {age} years old.")

# Other useful string methods
sample_text = "hello, world! how are you?"
print("\nOther useful methods:")
print("Count 'o':", sample_text.count('o'))
print("Find 'world':", sample_text.find('world'))
print("Is alphanumeric:", sample_text.isalnum())
print("Is alpha:", sample_text.isalpha())
print("Is digit:", sample_text.isdigit())
print("Is lower:", sample_text.islower())
print("Is upper:", sample_text.isupper())
print("Is space:", sample_text.isspace())
print("Starts with 'hello':", sample_text.startswith('hello'))
print("Ends with '?':", sample_text.endswith('?'))

# String encoding and decoding
encoded = "Pythön".encode('utf-8')
decoded = encoded.decode('utf-8')
print("\nEncoding and Decoding:")
print("Encoded:", encoded)
print("Decoded:", decoded)

# String comparison
str_a = "apple"
str_b = "banana"
print("\nString comparison:")
print("apple == banana:", str_a == str_b)
print("apple < banana:", str_a < str_b)

# Raw strings
raw_string = r"This is a raw string\n"
print("\nRaw string:", raw_string)

# String constants
import string
print("\nString constants:")
print("ASCII letters:", string.ascii_letters)
print("Digits:", string.digits)
print("Punctuation:", string.punctuation)

# String alignment
text = "Python"
print("\nString alignment:")
print("Center:", text.center(20, '*'))
print("Left justify:", text.ljust(20, '-'))
print("Right justify:", text.rjust(20, '+'))

# String translation
trans_table = str.maketrans("aeiou", "12345")
translated = "hello world".translate(trans_table)
print("\nString translation:", translated)
