# Example of lexical scope in Python

# Define a function with a local variable
def outer_function():
    # Local variable in the outer function
    outer_var = "This is a variable from the outer function."
    
    # Define an inner function
    def inner_function():
        # Accessing the local variable from the outer function
        print(outer_var)
    
    # Call the inner function to demonstrate lexical scope
    inner_function()

# Call the outer function to execute the inner function
outer_function()

