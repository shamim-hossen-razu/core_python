def append_to(element, to=[]):
    to.append(element)
    return to

my_list = append_to(12)
print(my_list)  # Output: [12]

my_other_list = append_to(42)
print(my_other_list)  # Output: [12, 42]

# To avoid this, use None as the default value and create a new list inside the function
def append_to(element, to=None):
    if to is None:
        to = []
    to.append(element)
    return to

my_list = append_to(12)
print(my_list)  # Output: [12]

my_other_list = append_to(42)
print(my_other_list)  # Output: [42]
