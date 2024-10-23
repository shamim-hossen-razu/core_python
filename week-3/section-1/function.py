def my_function():
    pass

print(callable(my_function))  # Output: True

def greet(name):
    print(f"Hello, {name}!")

def add_numbers(a, b):
    return a + b

def my_function_with_args(*args):
    for arg in args:
        print(arg)

def my_function_with_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

def my_function_with_both(a, b, *args, **kwargs):
    print(f"a: {a}, b: {b}")
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

def greet_with_default(name = "World", *args, **kwargs):
    print(f"Hello, {name}!", *args, **kwargs)

greet_with_default("John", "How are you?", age=30)  # Output: Hello, John! How are you? {'age': 30}

greet_with_default()  # Output: Hello, World!
greet_with_default("John")  # Output: Hello, John!




