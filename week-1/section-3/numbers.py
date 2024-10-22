# Numbers in Python

# Integer
x = 10
print(f"x is an integer: {x}")

# Float
y = 3.14
print(f"y is a float: {y}")

# Complex number
z = 2 + 3j
print(f"z is a complex number: {z}")

# Basic arithmetic operations
a = 5
b = 3
print(f"Addition: {a + b}")
print(f"Subtraction: {a - b}")
print(f"Multiplication: {a * b}")
print(f"Division: {a / b}")
print(f"Floor division: {a // b}")
print(f"Modulus: {a % b}")
print(f"Exponentiation: {a ** b}")

# Built-in functions for numbers
print(f"Absolute value of -5: {abs(-5)}")
print(f"Round 3.7: {round(3.7)}")
print(f"Round 3.14159 to 2 decimal places: {round(3.14159, 2)}")
print(f"Power of 2 to 3: {pow(2, 3)}")
print(f"Maximum of 5, 10, 15: {max(5, 10, 15)}")
print(f"Minimum of 5, 10, 15: {min(5, 10, 15)}")

# This behavior might seem inconsistent at first glance. You might expect both 2.5 and 3.5 to round up, but that's not what happens. Here's why:
# 1. Python uses a rounding strategy called "round half to even" or "banker's rounding".
# When a number is exactly halfway between two integers, it rounds to the nearest even integer.
# So 2.5 rounds down to 2 (the nearest even integer), while 3.5 rounds up to 4 (again, the nearest even integer).
# This method is designed to reduce bias in statistical sampling and financial calculations. It's not a "lie" or a bug, but it is a behavior that can surprise programmers who are used to always rounding .5 up.
# If you need different rounding behavior, you can implement your own rounding function or use the math.ceil() and math.floor() functions for specific cases.
print("\nRounding Quirk in Python:")
print(f"round(2.5) = {round(2.5)}")
print(f"round(3.5) = {round(3.5)}")


# Type conversion
float_num = 3.14
int_num = int(float_num)
print(f"Float to int: {int_num}")

str_num = "42"
int_from_str = int(str_num)
print(f"String to int: {int_from_str}")

# Number system conversions
decimal = 42
binary = bin(decimal)
octal = oct(decimal)
hexadecimal = hex(decimal)

print(f"Decimal 42 in binary: {binary}")
print(f"Decimal 42 in octal: {octal}")
print(f"Decimal 42 in hexadecimal: {hexadecimal}")

# Built-in number-related functions
print(f"Is 5 greater than 3? {bool(5 > 3)}")
print(f"Complex number from 3 and 4: {complex(3, 4)}")
print(f"Divmod of 17 and 5: {divmod(17, 5)}")

# Numeric type checking
print(f"Is 42 an instance of int? {isinstance(42, int)}")
print(f"Is 3.14 an instance of float? {isinstance(3.14, float)}")
print(f"Is 2+3j an instance of complex? {isinstance(2+3j, complex)}")


# Built-in constants
print(f"Value of True: {True}")
print(f"Value of False: {False}")
print(f"Value of None: {None}")

# Additional number operations
num = -4.3
print(f"Absolute value of {num}: {abs(num)}")
print(f"Round {num}: {round(num)}")
print(f"Round {num} to 1 decimal place: {round(num, 1)}")

# Checking for infinity and NaN
pos_inf = float('inf')
neg_inf = float('-inf')
not_a_number = float('nan')

print(f"Is {pos_inf} infinite? {pos_inf == float('inf')}")
print(f"Is {neg_inf} infinite? {neg_inf == float('-inf')}")
print(f"Is {not_a_number} NaN? {not_a_number != not_a_number}")  # NaN is the only value that doesn't equal itself

# float() is a built-in Python function that converts its argument to a floating-point number.
# 'nan' is a string that represents "Not a Number" in Python.
# When you pass 'nan' to the float() function, it creates a special floating-point value that represents an undefined or unrepresentable value.
# NaN has some unique properties:
# It's not equal to any value, including itself.
# Any arithmetic operation involving NaN results in NaN.
# It's used to represent undefined mathematical operations (like 0/0) or missing data in numerical computations.
# You can test for NaN using the math.isnan() function or by checking if a value is not equal to itself (which is only true for NaN):


