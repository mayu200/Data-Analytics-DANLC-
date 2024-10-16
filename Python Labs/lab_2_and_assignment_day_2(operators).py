# -*- coding: utf-8 -*-
"""LAB-2 and Assignment Day-2(Operators)

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wutrLWGr7WtkIa_jaSbmKzKXvZudPVmi

Mayuri Khatpe

*Q.1 Write a program for arithmatic operators*
"""

# Define two numbers
a = 10
b = 5

# Addition
addition = a + b
print("Addition:", addition)  # Output: 15

# Subtraction
subtraction = a - b
print("Subtraction:", subtraction)  # Output: 5

# Multiplication
multiplication = a * b
print("Multiplication:", multiplication)  # Output: 50

# Division
division = a / b
print("Division:", division)  # Output: 2.0

# Modulus (remainder of the division)
modulus = a % b
print("Modulus:", modulus)  # Output: 0

# Exponentiation (a raised to the power of b)
exponentiation = a ** b
print("Exponentiation:", exponentiation)  # Output: 100000

# Floor Division (division that rounds down to the nearest integer)
floor_division = a // b
print("Floor Division:", floor_division)  # Output: 2

"""Q.2 Write a program for assignment operators


"""

# Initialize a variable
a = 10
print("Initial value of a:", a)  # Output: 10

# Assignment with addition (a = a + 5)
a += 5
print("After a += 5:", a)  # Output: 15

# Assignment with subtraction (a = a - 3)
a -= 3
print("After a -= 3:", a)  # Output: 12

# Assignment with multiplication (a = a * 2)
a *= 2
print("After a *= 2:", a)  # Output: 24

# Assignment with division (a = a / 4)
a /= 4
print("After a /= 4:", a)  # Output: 6.0

# Assignment with modulus (a = a % 3)
a %= 3
print("After a %= 3:", a)  # Output: 0.0

# Assignment with exponentiation (a = a ** 2)
a = 4  # Reset a to 4 for this operation
a **= 2
print("After a **= 2:", a)  # Output: 16

# Assignment with floor division (a = a // 3)
a //= 3
print("After a //= 3:", a)  # Output: 5

"""Q.3Write a program for Bitwise operators

Explanation:
Bitwise AND (&): Compares each bit of the two numbers and returns 1 if both bits are 1, otherwise 0.

Bitwise OR (|): Compares each bit of the two numbers and returns 1 if at least one of the bits is 1.

Bitwise XOR (^): Compares each bit of the two numbers and returns 1 if the bits are different, otherwise 0.

Bitwise NOT (~): Inverts the bits of the number. The result is -(n + 1) for a given number n.

Left Shift (<<): Shifts the bits of the number to the left by the specified number of positions. Each shift to the left doubles the number.

Right Shift (>>): Shifts the bits of the number to the right by the specified number of positions. Each shift to the right halves the number.
"""

# Bitwise Operators in Python

# Define two numbers
a = 10  # Binary: 1010
b = 4   # Binary: 0100

# Bitwise AND
bitwise_and = a & b
print("Bitwise AND (a & b):", bitwise_and)  # Output: 0 (Binary: 0000)

# Bitwise OR
bitwise_or = a | b
print("Bitwise OR (a | b):", bitwise_or)  # Output: 14 (Binary: 1110)

# Bitwise XOR
bitwise_xor = a ^ b
print("Bitwise XOR (a ^ b):", bitwise_xor)  # Output: 14 (Binary: 1110)

# Bitwise NOT
bitwise_not = ~a
print("Bitwise NOT (~a):", bitwise_not)  # Output: -11 (Binary: 1111...0101)

# Bitwise Left Shift
left_shift = a << 2
print("Left Shift (a << 2):", left_shift)  # Output: 40 (Binary: 101000)

# Bitwise Right Shift
right_shift = a >> 2
print("Right Shift (a >> 2):", right_shift)  # Output: 2 (Binary: 0010)

"""Q.4 Write a program to calculate greatest of three numbers.

1.      Calculate the area of a circle.

2.      Calculate the area of a triangle.

3.      Calculate the area of a rectangle.

4.      Calculate the area of a square.

Q.4 Write a program to calculate greatest of three numbers.
"""

# Program to find the greatest of three numbers

# Input three numbers
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))

# Determine the greatest number
if a >= b and a >= c:
    greatest = a
elif b >= a and b >= c:
    greatest = b
else:
    greatest = c

# Output the result
print("The greatest number is:", greatest)

"""Area of a Circle:

"""

import math

# Program to calculate the area of a circle
radius = float(input("Enter the radius of the circle: "))
area_circle = math.pi * radius ** 2
print("The area of the circle is:", area_circle)

"""Area of a Triangle:

"""

# Program to calculate the area of a triangle

# Input the base and height of the triangle
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

# Calculate the area
area_triangle = 0.5 * base * height
print("The area of the triangle is:", area_triangle)

"""Area of a Rectangle:

"""

# Program to calculate the area of a rectangle

# Input the length and width of the rectangle
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculate the area
area_rectangle = length * width
print("The area of the rectangle is:", area_rectangle)

"""Area of a Square:

"""

# Program to calculate the area of a square

# Input the side length of the square
side = float(input("Enter the side length of the square: "))

# Calculate the area
area_square = side ** 2
print("The area of the square is:", area_square)

"""LAB-2

1. Calculate the multiplication and sum of two numbers
"""

# Define the two numbers
a = 5
b = 3

# Calculate multiplication
multiplication_result = a * b

# Calculate sum
sum_result = a + b

# Print the results
print("Multiplication:", multiplication_result)
print("Sum:", sum_result)

""" 2. Declare two variables and print that which variable is largest using ternary operators


"""

# Declare two variables
a = 10
b = 20

# Use a ternary operator to determine the largest variable
largest = a if a > b else b

# Print the result
print("The largest variable is:", largest)

"""3. Python program to convert the temperature in degree centigrade to Fahrenheit


"""

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Input temperature in Celsius
celsius_temp = float(input("Enter temperature in Celsius: "))

# Convert to Fahrenheit
fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)

# Print the result
print(f"Temperature in Fahrenheit: {fahrenheit_temp}")

"""4. Python program to find the area of a triangle whose sides are given


"""

import math

# Function to calculate the area of a triangle using Heron's formula
def triangle_area(a, b, c):
    # Calculate the semi-perimeter
    s = (a + b + c) / 2

    # Calculate the area
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

# Input the lengths of the sides
a = float(input("Enter the length of the first side: "))
b = float(input("Enter the length of the second side: "))
c = float(input("Enter the length of the third side: "))

# Check if the sides form a valid triangle
if a + b > c and b + c > a and a + c > b:
    # Calculate the area
    area = triangle_area(a, b, c)
    print(f"The area of the triangle is: {area:.2f}")
else:
    print("The given sides do not form a valid triangle.")