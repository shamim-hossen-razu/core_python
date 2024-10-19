from local_math import basic_math, advanced_math
from local_math.geometry import circle, square
from local_math.geometry.analytic_geometry import coordinates
if __name__ == "__main__":
    print('Sum of 16 and 3:', basic_math.add(16, 3))
    print('Difference of 16 and 3:', basic_math.subtract(16, 3))
    print('Product of 16 and 3:', basic_math.multiply(16, 3))
    print('Division of 16 and 3:', basic_math.divide(16, 3))
    print('Cube of 16:', advanced_math.cube(16))
    print('Factorial of 3:', advanced_math.factorial(3))
    print('Square root of 5:', advanced_math.square_root(5))
    print('Area of circle with radius 5:', circle.area(5))
    print('Area of square with side length 4:', square.area(4))
    print('Distance between points (1, 2) and (4, 6):', coordinates.distance_between_points(1, 2, 4, 6))
    print('Midpoint between points (1, 2) and (4, 6):', coordinates.midpoint(1, 2, 4, 6))
#
