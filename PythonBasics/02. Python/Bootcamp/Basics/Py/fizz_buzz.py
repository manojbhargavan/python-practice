# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 19:08:30 2023

@author: manoj
"""

def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        print(f"{i}\tFizzBuzz")
    elif number % 3 == 0:
        print(f"{i}\tFizz")
    elif number % 5 == 0:
        print(f"{i}\tBuzz")
    else:
        print(i)

number = int(input("Please enter a number: "))

for i in range(1, number + 1):
    fizz_buzz(i)
    

