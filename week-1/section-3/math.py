import math

# Constants
print(f"Pi: {math.pi}")
print(f"Euler's number: {math.e}")
print(f"Tau (2*pi): {math.tau}")
print(f"Infinity: {math.inf}")
print(f"Not a Number (NaN): {math.nan}")

# Basic functions
print(f"Square root of 16: {math.sqrt(16)}")
print(f"Absolute value of -5: {math.fabs(-5)}")
print(f"Factorial of 5: {math.factorial(5)}")
print(f"GCD of 48 and 18: {math.gcd(48, 18)}")
print(f"LCM of 15 and 20: {math.lcm(15, 20)}")  # New in Python 3.9+

# Exponential and logarithmic functions
print(f"e^2: {math.exp(2)}")
print(f"Natural log of 10: {math.log(10)}")
print(f"Log base 2 of 8: {math.log2(8)}")
print(f"Log base 10 of 100: {math.log10(100)}")

# Trigonometric functions (input in radians)
print(f"Sin of pi/2: {math.sin(math.pi/2)}")
print(f"Cos of pi: {math.cos(math.pi)}")
print(f"Tan of pi/4: {math.tan(math.pi/4)}")

# Inverse trigonometric functions (return value in radians)
print(f"Arcsin of 1: {math.asin(1)}")
print(f"Arccos of -1: {math.acos(-1)}")
print(f"Arctan of 1: {math.atan(1)}")
print(f"Atan2 of (1, 1): {math.atan2(1, 1)}")

# Hyperbolic functions
print(f"Sinh of 1: {math.sinh(1)}")
print(f"Cosh of 0: {math.cosh(0)}")
print(f"Tanh of 0: {math.tanh(0)}")

# Inverse hyperbolic functions
print(f"Asinh of 1: {math.asinh(1)}")
print(f"Acosh of 2: {math.acosh(2)}")
print(f"Atanh of 0.5: {math.atanh(0.5)}")

# Angular conversion
print(f"30 degrees to radians: {math.radians(30)}")
print(f"pi/4 radians to degrees: {math.degrees(math.pi/4)}")

# Ceiling and floor
print(f"Ceiling of 3.7: {math.ceil(3.7)}")
print(f"Floor of 3.7: {math.floor(3.7)}")

# Power and exponential functions
print(f"2^3: {math.pow(2, 3)}")
print(f"e^2: {math.exp(2)}")
print(f"2^3 - 1: {math.expm1(3)}")  # e^x - 1

# Rounding functions
print(f"Truncate 3.7: {math.trunc(3.7)}")
print(f"Round 3.7 to nearest integer: {round(3.7)}")

# Other functions
print(f"Hypotenuse of 3 and 4: {math.hypot(3, 4)}")
print(f"Is 5 close to 5.00001? {math.isclose(5, 5.00001)}")
print(f"Gamma function of 5: {math.gamma(5)}")
print(f"Error function of 1: {math.erf(1)}")
print(f"Complementary error function of 1: {math.erfc(1)}")

# Check for special values
print(f"Is pi finite? {math.isfinite(math.pi)}")
print(f"Is inf infinite? {math.isinf(math.inf)}")
print(f"Is nan a NaN? {math.isnan(math.nan)}")

# Combinatorics
print(f"Permutations of 5 choose 3: {math.perm(5, 3)}")
print(f"Combinations of 5 choose 3: {math.comb(5, 3)}")

# Floating-point operations
print(f"Next float up from 1.0: {math.nextafter(1.0, 2.0)}")
print(f"Next float down from 1.0: {math.nextafter(1.0, 0.0)}")
print(f"Ulp of 1.0: {math.ulp(1.0)}")

# Special mathematical functions
print(f"Bessel function J0(1): {math.j0(1)}")
print(f"Bessel function J1(1): {math.j1(1)}")
print(f"Bessel function Y0(1): {math.y0(1)}")
print(f"Bessel function Y1(1): {math.y1(1)}")

# Constants
print(f"Machine epsilon: {math.epsilon}")

