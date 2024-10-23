def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a  # Yield the current value of a
        a, b = b, a + b  # Update a and b to the next Fibonacci numbers

def simple_generator(n):
    i = 0
    while i <= n:
        yield i
        i = i + 1

# Using the generator
n = 10
print(f"First {n} Fibonacci numbers:")
for number in fibonacci(n):
    print(number)

x = simple_generator(n)
print(x)
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__iter__())