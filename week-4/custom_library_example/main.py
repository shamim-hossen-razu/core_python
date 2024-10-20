import local_math_library

if __name__ == "__main__":
    print('Sum of 16 and 3:', local_math_library.add(16, 3))
    print('Difference of 16 and 3:', local_math_library.basic_math.subtract(16, 3))
    print('Product of 16 and 3:', local_math_library.basic_math.multiply(16, 3))
    print('Division of 16 and 3:', local_math_library.basic_math.divide(16, 3))
    print('Cube of 16:', local_math_library.advanced_math.cube(16))
    print('Factorial of 3:', local_math_library.advanced_math.factorial(3))
    print('Square root of 5:', local_math_library.advanced_math.square_root(5))
    print('Area of circle with radius 5:', local_math_library.circle_area(5))
    print('Area of square with side length 4:', local_math_library.square_area(4))
