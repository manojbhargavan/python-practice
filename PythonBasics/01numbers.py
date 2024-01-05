# Run in shell: python Basics/01numbers.py
# Integer and Floating point Numbers

# Integer
a: int = 22
b: int = 7
print(a + b, a - b, a * b, a / b)

# Data Type of a and a/b
print(type(a))
print(type(a/b))

# Floating point
PI = 22/7
radius = float(input('Enter radius of circle: '))
area = PI * radius ** 2 # ** is exponentiation operator, radius^2
print(f'Area of circle is {area}')

# Floating Point Division
print(22/7)
# Integer Division
print(22//7)
# Remainder
print(22 % 7)
