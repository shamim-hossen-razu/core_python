
def square_root(x):
    return x ** 0.5

def cube(x):
    return x ** 3

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
