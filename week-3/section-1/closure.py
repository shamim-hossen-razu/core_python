# Example of closure in Python

# A closure is a function that has access to its own scope, as well as the scope of its outer functions.

# Function 1: Outer function
def outer_function(msg):
    # Define an inner function
    def inner_function():
        # Accessing the variable from the outer function
        print(msg)
    
    # Return the inner function
    return inner_function

# Create a closure by calling the outer function
hello = outer_function("Hello, world!")
goodbye = outer_function("Goodbye, world!")

# Call the closure
hello()  # Output: Hello, world!
goodbye()  # Output: Goodbye, world!

# Function 2: Counter example
def counter():
    count = 0
    def increment():
        nonlocal count  # Use the count variable from the outer function
        count += 1
        return count
    return increment

# Create a counter closure
counter1 = counter()
counter2 = counter()

# Use the counter closures
print(counter1())  # Output: 1
print(counter1())  # Output: 2
print(counter2())  # Output: 1
print(counter2())  # Output: 2

# Function 3: Bank account example
def bank_account(initial_balance):
    balance = initial_balance
    def deposit(amount):
        nonlocal balance
        balance += amount
        return balance
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            print("Insufficient funds")
        else:
            balance -= amount
            return balance
    return deposit, withdraw

# Create a bank account closure
deposit, withdraw = bank_account(1000)

# Use the bank account closures
print(deposit(500))  # Output: 1500
print(withdraw(200))  # Output: 1300
print(withdraw(1500))  # Output: Insufficient funds

