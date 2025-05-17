# Topic 4 exercises 
# Topic 4: Functions & Modules

# Task 1: Define and call a simple function
def greet(name):
    """Return a greeting for the given name."""
    return f"Hello, {name}!"

print(greet("Vennela Tata"))

# Task 2: Function with parameters and return value
def rectangle_area(width, height):
    """Calculate area of a rectangle."""
    return width * height

w, h = 4, 7
print(f"Area of {w}x{h} rectangle is {rectangle_area(w, h)}")

# Task 3: Import and use a standard library module
import math
print("Square root of 16 is", math.sqrt(16))
print("Value of pi is", math.pi)

# Task 4: Importing your own module (myutils.py)
from myutils import add, multiply
print("3 + 5 =", add(3, 5))
print("4 * 6 =", multiply(4, 6))
