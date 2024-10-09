# -*- coding: utf-8 -*-
"""Lab 12 For loop

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/110x5MMxi0y2GdBKdynpYSuoNtMU6hf7V

MAYURI KHATPE

Print the first 10 natural numbers using a for loop:
"""

for i in range(1, 11):
    print(i)

"""Python program to check if the given string is a palindrome:

"""

def is_palindrome(string):
    if string == string[::-1]:
        print(f"'{string}' is a palindrome")
    else:
        print(f"'{string}' is not a palindrome")

# Input from user
string = input("Enter a string: ")
is_palindrome(string)

"""Python program to check if a given number is an Armstrong number:

"""

def is_armstrong(num):
    digits = [int(digit) for digit in str(num)]
    armstrong_sum = sum([digit ** len(digits) for digit in digits])

    if num == armstrong_sum:
        print(f"{num} is an Armstrong number")
    else:
        print(f"{num} is not an Armstrong number")

# Input from user
num = int(input("Enter a number: "))
is_armstrong(num)

"""Python program to get the Fibonacci series between 0 and 50:

"""

a, b = 0, 1
while a <= 50:
    print(a, end=" ")
    a, b = b, a + b

"""Python program to check the validity of password input by users:

"""

import re

def is_valid_password(password):
    if (len(password) >= 6 and len(password) <= 12 and
        re.search("[a-z]", password) and
        re.search("[A-Z]", password) and
        re.search("[0-9]", password) and
        re.search("[$#@]", password)):
        print("Password is valid")
    else:
        print("Password is not valid")

# Input from user
password = input("Enter a password: ")
is_valid_password(password)