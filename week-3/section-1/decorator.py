# Define a decorator function that takes a function as an argument
def my_decorator(func):
    # Define a wrapper function that will be returned by the decorator
    def wrapper():
        # Code to be executed before the function call
        print("Something is happening before the function is called.")
        # Call the original function
        func()
        # Code to be executed after the function call
        print("Something is happening after the function is called.")
    # Return the wrapper function
    return wrapper

# Define a function that will be decorated
@my_decorator
def say_hello():
    # This is the function that will be decorated
    print("Hello!")

# Call the decorated function
say_hello()

# Define another function that will be decorated
@my_decorator
def say_goodbye():
    # This is the function that will be decorated
    print("Goodbye!")

# Call the decorated function
say_goodbye()

# Define another function that will be decorated
@my_decorator
def say_morning():
    # This is the function that will be decorated
    print("Good morning!")

# Call the decorated function
say_morning()


# Example of a decorator that logs the execution time of a function
import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Start timing
        result = func(*args, **kwargs)  # Call the original function with arguments
        end_time = time.time()  # Stop timing
        print(f"{func.__name__} executed in {end_time - start_time} seconds")
        return result  # Return the result of the original function
    return wrapper

def example_function(name):
    # Simulate some time-consuming operation
    time.sleep(2)  # Sleep for 2 seconds to simulate a time-consuming operation
    print(f"Hello, {name}!")

decorated_example_function = timer_decorator(example_function)
decorated_example_function("Alice")

