# Local Math Library

## Overview

Local Math Library is a custom Python package that provides various mathematical operations and geometric calculations. It's designed to be a simple, easy-to-use library for basic and advanced mathematical computations.

## Features

The library includes the following modules:

1. Basic Math Operations
   - Addition
   - Subtraction
   - Multiplication
   - Division

2. Advanced Math Operations
   - Cube
   - Factorial
   - Square Root

3. Geometry
   - Circle area calculation
   - Square area calculation

4. Analytic Geometry
   - Distance between two points
   - Midpoint calculation

## Installation

To install the Local Math Library, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/shamim-hossen-razu/core_python.git
   ```

2. Navigate to the custom library example directory:
   ```
   cd core_python/week-4/custom_library_example
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Build and install the library:
   ```
   python setup.py sdist bdist_wheel
   pip install dist/local_math_library-0.1.0-py3-none-any.whl
   ```

Now you can use the Local Math Library in your Python projects.

## Distribution

If you want to distribute this package, follow these additional steps:

1. Ensure you have the latest versions of setuptools and wheel:
   ```
   pip install --upgrade setuptools wheel
   ```

2. Build the distribution packages:
   ```
   python setup.py sdist bdist_wheel
   ```

3. Install and upgrade twine:
   ```
   pip install --upgrade twine
   ```

4. Upload the distribution packages to PyPI:
   ```
   twine upload dist/*
   ```

   Note: You'll need to have a PyPI account and be registered as a maintainer of the project to upload the package.

5. Once uploaded, users can install your package using pip:
   ```
   pip install local_math_library
   ```

Remember to update the version number in `setup.py` each time you make changes and want to distribute a new version of the package.
