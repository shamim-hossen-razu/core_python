def my_function():
    pass

print(type(my_function))  # Output: <class 'function'>

# Functions are objects, so you can assign them to variables
func = my_function
print(type(func))  # Output: <class 'function'>

# You can also pass functions as arguments to other functions
def execute_function(func):
    func()

execute_function(my_function)

# And you can return functions from other functions
def return_function():
    def inner_function():
        print("Hello from inner function!")
    return inner_function

returned_func = return_function()
returned_func()  # Output: Hello from inner function!

print(my_function.__doc__)  # Output: None
print(my_function.__name__)  # Output: my_function
print(my_function.__qualname__)  # Output: my_function
print(my_function.__module__)  # Output: __main__
print(my_function.__defaults__)  # Output: None
print(my_function.__code__)  # Output: <code_object <module>
print(my_function.__globals__)  # Output: {...} (global variables)
print(my_function.__dict__)  # Output: {} (function attributes)
print(my_function.__closure__)  # Output: None


