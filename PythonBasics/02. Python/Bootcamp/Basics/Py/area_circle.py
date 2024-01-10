# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 11:19:51 2023

@author: manoj
"""

# # Ask use of radius of circle and calculate the area
# radius = float(input('What is the radius of the circle?\n >>> '))
# pi = 22/7
# area = pi * radius**2
# print('Radius = ', radius, ', Area of Circle = ', area)

# # F to C
# far = float(input('Please enter the temprature in Fahrenheit\n >>> '))
# cel = (far - 32) * 5/9
# print('Fahrenheit: ', far, ', Celsius: ', cel)

# Add two numbers from user
# num_1 = int(input('First Number Please\n >>> '))
# num_2 = int(input('Second Number Please\n >>> '))
# result_add = num_1 + num_2
# result_product = num_1 * num_2
# print('Number 1: ', num_1, ', Number 2: ', num_2, ', Sum: ', result_add, ', Product: ', result_product)

# 4 Person need 4 slice of pizza each, local pizza guy sells 6 slice an order
num_persons = 4
per_person_consumption = 4
local_pizza_order_size = 6
total_slices_needed = num_persons * per_person_consumption

number_of_orders = total_slices_needed//local_pizza_order_size + 1
wasted_portion = (local_pizza_order_size * number_of_orders) - total_slices_needed
print(f'Need {number_of_orders} Order (Slices: {local_pizza_order_size * number_of_orders}), Wasted Slices: {wasted_portion}')
