# Topic 2 exercises 
# Topic 2: Basic Data Types & Operators

# Task 1: area and perimeter of a rectangle
width = 5
height = 3
area = width * height
perimeter = 2 * (width + height)
print(f"Area: {area}, Perimeter: {perimeter}")

# Task 2: compare two numbers
a = 10
b = 7
if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is less than {b}")
else:
    print(f"{a} is equal to {b}")

# Task 3: check leap year
year = 2024
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print(f"{year} is a leap year: {is_leap}")

# Task 5: concatenate two strings
s1 = "TSX"
s2 = "Unstop"
print(s1 + " " + s2)
