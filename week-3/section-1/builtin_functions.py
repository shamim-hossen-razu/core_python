# Example of all the built-in functions in Python

# 1. abs() - Returns the absolute value of a number
print(abs(-5))  # Output: 5

# 2. all() - Returns True if all elements of an iterable are true
print(all([True, True, True]))  # Output: True
print(all([True, False, True]))  # Output: False

# 3. any() - Returns True if any element of an iterable is true
print(any([True, True, True]))  # Output: True
print(any([True, False, True]))  # Output: True
print(any([False, False, False]))  # Output: False

# 4. ascii() - Returns a string containing a printable representation of an object
print(ascii("Hello, World!"))  # Output: 'Hello, World!'

# 5. bin() - Converts an integer to a binary string
print(bin(10))  # Output: 0b1010

# 6. bool() - Converts a value to a boolean
print(bool(5))  # Output: True
print(bool(0))  # Output: False

# 7. bytearray() - Returns a bytearray object
print(bytearray(b'Hello, World!'))  # Output: bytearray(b'Hello, World!')

# 8. bytes() - Returns a bytes object
print(bytes(b'Hello, World!'))  # Output: b'Hello, World!'

# 9. callable() - Returns True if the object is callable, otherwise False
print(callable(lambda x: x))  # Output: True
print(callable("Hello, World!"))  # Output: False

# 10. chr() - Returns a string representing a character whose Unicode code point is the integer
print(chr(65))  # Output: A

# 11. classmethod() - Converts a function to be a class method
class MyClass:
    @classmethod
    def my_class_method(cls):
        print("This is a class method.")
MyClass.my_class_method()  # Output: This is a class method.

# 12. compile() - Parses the source into a code or AST node
source = "print('Hello, World!')"
code = compile(source, '<string>', 'exec')
exec(code)  # Output: Hello, World!

# 13. complex() - Creates a complex number
print(complex(3, 4))  # Output: (3+4j)

# 14. dict() - Creates a dictionary
print(dict(a=1, b=2, c=3))  # Output: {'a': 1, 'b': 2, 'c': 3}

# 15. dir() - Returns a list of names in the current local scope
print(dir())  # Output: ['__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']

# 16. divmod() - Returns the quotient and remainder when dividing two numbers
print(divmod(17, 5))  # Output: (3, 2)

# 17. enumerate() - Returns an enumerate object
for i, value in enumerate(['a', 'b', 'c']):
    print(f"Index: {i}, Value: {value}")

# 18. eval() - Parses the expression passed to this method and executes Python expression(s) passed as a string
print(eval("1 + 2"))  # Output: 3

# 19. filter() - Constructs an iterator from elements of an iterable for which a function returns true
def is_even(num):
    return num % 2 == 0
print(list(filter(is_even, [1, 2, 3, 4, 5, 6])))  # Output: [2, 4, 6]

# 20. float() - Converts a value to a floating point number
print(float(5))  # Output: 5.0

# 21. format() - Formats a string with variables
print("Hello, {}".format("World!"))  # Output: Hello, World!

# 22. frozenset() - Returns a frozenset object
print(frozenset([1, 2, 3, 2, 3, 4, 5]))  # Output: frozenset({1, 2, 3, 4, 5})

# 23. getattr() - Returns the value of a named attribute of an object
class MyClass:
    def __init__(self):
        self.my_attribute = "Hello, World!"
print(getattr(MyClass(), 'my_attribute'))  # Output: Hello, World!

# 24. hasattr() - Returns True if the object has the named attribute
print(hasattr(MyClass(), 'my_attribute'))  # Output: True

# 25. hash() - Returns the hash value of an object
print(hash("Hello, World!"))  # Output: -1717744444

# 26. help() - Invokes the built-in help system
help()  # Output: Opens the help system

# 27. hex() - Converts an integer to a hexadecimal string
print(hex(10))  # Output: 0xa

# 28. id() - Returns the “identity” of the object
print(id("Hello, World!"))  # Output: 1402341234 (example)

# 29. input() - Reads a line from input, converts into a string, and returns that string
user_input = input("Enter your name: ")
print(f"Hello, {user_input}!")

# 30. int() - Converts a value to an integer
print(int("5"))  # Output: 5

# 31. isinstance() - Checks if the object is an instance of the class or a subclass thereof
print(isinstance("Hello, World!", str))  # Output: True

# 32. issubclass() - Checks if a class is a subclass of another class
class MyClass:
    pass
class MySubClass(MyClass):
    pass
print(issubclass(MySubClass, MyClass))  # Output: True

# 33. iter() - Returns an iterator object
my_list = [1, 2, 3, 4, 5]
my_iter = iter(my_list)
print(next(my_iter))  # Output: 1

# 34. len() - Returns the length of an object
print(len("Hello, World!"))  # Output: 13

# 35. list() - Creates a list
print(list("Hello, World!"))  # Output: ['H', 'e', 'l', 'l', 'o', ',', ' ', 'W', 'o', 'r', 'l', 'd', '!']

# 36. locals() - Updates and returns a dictionary of the current local symbol table
print(locals())  # Output: {'__name__': '__main__', '__doc__': None, '__package__': None}

# 37. map() - Applies a given function to each item of an iterable and returns a list of the results
def square(num):
    return num ** 2
print(list(map(square, [1, 2, 3, 4, 5])))  # Output: [1, 4, 9, 16, 25]

# 38. max() - Returns the largest item in an iterable or the largest of two or more arguments
print(max([1, 2, 3, 4, 5]))  # Output: 5

# 39. memoryview() - Returns a memory view object
print(memoryview(b'Hello, World!'))  # Output: <memory at 0x...>

# 40. min() - Returns the smallest item in an iterable or the smallest of two or more arguments
print(min([1, 2, 3, 4, 5]))  # Output: 1

# 41. next() - Retrieves the next item from an iterator by calling its __next__() method
my_list = [1, 2, 3, 4, 5]
my_iter = iter(my_list)
print(next(my_iter))  # Output: 1

# 42. object() - Returns a new featureless object
print(object())  # Output: <object object at 0x...>

# 43. oct() - Converts an integer to an octal string
print(oct(10))  # Output: 0o12

# 44. open() - Opens a file and returns a file object
with open("example.txt", "r") as file:
    print(file.read())  # Output: File content

# 45. ord() - Returns an integer representing the Unicode character
print(ord('A'))  # Output: 65

# 46. pow() - Returns the value of x to the power of y
print(pow(2, 3))  # Output: 8

# 47. print() - Prints objects to the text stream file
print("Hello, World!")  # Output: Hello, World!

# 48. property() - Returns a property attribute
class MyClass:
    def __init__(self):
        self._my_attribute = "Hello, World!"
    @property
    def my_attribute(self):
        return self._my_attribute
print(MyClass().my_attribute)  # Output: Hello, World!

# 49. range() - Returns a sequence of numbers starting from the first argument up to but not including the second argument
print(list(range(1, 6)))  # Output: [1, 2, 3, 4, 5]

# 50. repr() - Returns a string that is a valid Python expression
print(repr("Hello, World!"))  # Output: 'Hello, World!'

# 51. reversed() - Returns a reverse iterator
print(list(reversed([1, 2, 3, 4, 5])))  # Output: [5, 4, 3, 2, 1]

# 52. round() - Returns the floating point value number rounded to ndigits digits after the decimal point
print(round(3.141592653589793, 2))  # Output: 3.14

# 53. set() - Creates a set
print(set([1, 2, 3, 2, 3, 4, 5]))  # Output: {1, 2, 3, 4, 5}

# 54. setattr() - Sets the value of a named attribute of an object
class MyClass:
    pass
setattr(MyClass, 'my_attribute', "Hello, World!")
print(MyClass.my_attribute)  # Output: Hello, World!

# 55. slice() - Creates a slice object
print(slice(1, 5, 2))  # Output: slice(1, 5, 2)

# 56. sorted() - Returns a new sorted list from the elements of any sequence
print(sorted([5, 2, 8, 3, 1, 4]))  # Output: [1, 2, 3, 4, 5, 8]

# 57. staticmethod() - Converts a function to be a static method
class MyClass:
    @staticmethod
    def my_static_method():
        print("This is a static method.")
MyClass.my_static_method()  # Output: This is a static method.

# 58. str() - Converts a value to a string
print(str(5))  # Output: 5

# 59. sum() - Returns the sum of all items in an iterable
print(sum([1, 2, 3, 4, 5]))  # Output: 15

# 60. super() - Returns a proxy object that allows you to call methods of a parent class
class MyClass:
    def my_method(self):
        print("This is a method of MyClass.")
class MySubClass(MyClass):
    def my_method(self):
        super().my_method()
        print("This is a method of MySubClass.")
MySubClass().my_method()  # Output: This is a method of MyClass. This is a method of MySubClass.

# 61. tuple() - Creates a tuple
print(tuple("Hello, World!"))  # Output: ('H', 'e', 'l', 'l', 'o', ',', ' ', 'W', 'o', 'r', 'l', 'd', '!')

# 62. type() - Returns the type of an object
print(type("Hello, World!"))  # Output: <class 'str'>

# 63. vars() - Returns the __dict__ attribute of the current module
print(vars())  # Output: {...} (module variables)

# 64. zip() - Makes an iterator that aggregates elements from each of the iterables
print(list(zip([1, 2, 3], ['a', 'b', 'c'])))  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]
