#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 08:50:32 2019

@author: Manoj
"""

'''
Question 1
Ask the user for two numbers between 1 and 100. Then count from the
lower number to the higher number. Print the results to the screen.
'''
# def get_number_between(num1, num2):
#     number = int(input(f"Enter a number between {num1} and {num2}: "))
#     while not (number >= num1 and number <= num2):
#         number = int(input(f"Enter a number between {num1} and {num2}: "))
#     return number

# num1 = get_number_between(1, 100)
# num2 = get_number_between(1, 100)
# if num1 >= num2:
#     print("Not able to print from lower number to higher")
# else:
#     while num2 >= num1:
#         print(num2)
#         num2 -= 1


'''
Question 2
Ask the user to input a string and then print it out to the screen in
reverse order (use a for loop).
'''
# user_str = input("Enter a string: ")
# output = ""
# length = len(user_str) - 1
# while length >= 0:
#     output += user_str[length]
#     length -= 1
# print(output)


'''
Question 3
Ask the user for a number between 1 and 12 and then display a times
table for that number.
'''
# number = get_number_between(1, 12)
# for i in range(1, 13):
#     print(f"{number} x {i} = {number * i}")

'''
Question 4
Can you amend the solution to question 3 so that it just prints out all
times tables between 1 and 12? (no  need to ask user for input)
'''
# for i in range(1, 13):
#     print("-----------------")
#     print(f"Table of {i}")
#     print("-----------------")
#     for j in range(1, 13):
#         print(f"{i} x {j} = {i * j}")
#     print("-----------------\n")


'''
Question 5
Ask the user to input a sequence of numbers. Then calculate the mean
and print the result
'''
# user_input = "rand"
# total = 0
# number_count = 0
# while True:
#     user_input = input("Enter a number (press enter to exit): ")
#     if user_input == "":
#         break
#     total += int(user_input)
#     number_count += 1

# print(f"Mean: {total/number_count}")

'''
Question 6
Write code that will calculate 15 factorial. (factorial is product of
positive ints up to a given number. e.g 5 factorial is 5x4x3x2x1)
'''
# result = 1
# factorial_of = 15
# for i in range(2, factorial_of + 1):
#     result *= i
    
# print(result)

'''
Question 7
Write code to calculate Fibonacci numbers. Create list containing
first 20 Fibonacci numbers, (Fib  numbers made by sum of preceeding
two. Series starts 0 1 1 2 3 5 8 13 ....)
'''
# previous = 0
# current = 1
# limit = 13
# for i in range(0, limit + 1):
#     print(previous)
#     (previous, current) = (current, previous + current)


'''
Question 8
The previous question was the first to contain comments. Go back
through the other questions in this file and add comments to the
solutions.
'''


'''
Question 9

     *****
     *
     ****
     *
     *
     *
Can you draw this using python? (comment the solution code)
'''
# print("     *****")
# print("     *")
# print("     ****")
# print("     *")
# print("     *")
# print("     *")


'''
Question 10
Write some code that will determine all odd and even numbers
between 1 and 100. Put the odds in a list named odd and the evens
in a list named even.
'''
odd = list()
even = list()

for i in range(1, 101):
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print(even)
print(odd)
