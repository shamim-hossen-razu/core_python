
"""
Local Math Library

This library provides a collection of mathematical functions and geometric calculations.

Modules:
- basic_math: Basic arithmetic operations (add, subtract, multiply, divide)
- advanced_math: Advanced mathematical operations (cube, factorial, square_root)
- geometry: Geometric calculations for circles and squares
- geometry.analytic_geometry: Analytic geometry calculations (distance between points, midpoint)

Usage:
    from local_math_library import add, subtract, multiply, divide
    from local_math_library import cube, factorial, square_root
    from local_math_library.geometry import circle, square
    from local_math_library.geometry.analytic_geometry import distance_between_points, midpoint

For more detailed information, refer to the individual module docstrings.
"""


# Import all modules from the local_math_library package
from local_math_library.basic_math import add, subtract, multiply, divide
from local_math_library.advanced_math import cube, factorial, square_root
from local_math_library.geometry import circle_area, square_area
from local_math_library.geometry.analytic_geometry import distance_between_points, midpoint

__all__ = [add, subtract, multiply, divide, cube, factorial, square_root, circle_area, square_area, distance_between_points, midpoint]