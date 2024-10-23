def implicit_return_example():
    # In Python, if a function doesn't explicitly return a value, it will implicitly return None
    pass

print(implicit_return_example())  # Output: None


def early_return_example():
    # If a condition is met, the function will return early
    if True:
        return "Early return"
    # If the condition is not met, the function will continue to execute
    print("This will not be printed")
    return "Normal return"

print(early_return_example())  # Output: Early return

def return_multiple_values():
    # In Python, you can return multiple values from a function using tuples, lists, or dictionaries
    return "value1", "value2", "value3"

# Make a function call and unpack the returned values
value1, value2, value3 = return_multiple_values()
print("Value 1:", value1)
print("Value 2:", value2)
print("Value 3:", value3)

# Alternatively, you can return a list or dictionary and access the values by index or key
def return_list():
    return ["value1", "value2", "value3"]

def return_dict():
    return {"key1": "value1", "key2": "value2", "key3": "value3"}

list_values = return_list()
dict_values = return_dict()

print("List Values:", list_values)
print("Dictionary Values:", dict_values)




