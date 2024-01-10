# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 17:32:12 2019

@author: giles
"""

'''
Question 1
Can you remember how to check if a key exists in a dictionary?
Using the capitals dictionary below write some code to ask the user to input
a country, then check to see if that country is in the dictionary and if it is
print the capital. If not tell the user it's not there.
'''
# countries = {
#     'france': {'capital': 'Paris', 'language': 'French'},
#     'united kingdom': {'capital': 'London', 'language': 'English'},
#     'united states of america': {'capital': 'Washington DC', 'language': 'English'},
#     'italy': {'capital': 'Rome', 'language': 'Italian'},
#     'india': {'capital': 'Delhi', 'language': 'Hindi, Tamil, Malayalam, Bengali, Assamese, Oriya, Marathi, Telugu, Kannada, Punjabi, Gujarati, Urdu, Sindhi, Kashmiri, Nepali, Konkani, Sindhi, Dogri, Maithili, Santali, Manipuri, Bodo, and various others'},
#     'canada': {'capital': 'Ottawa', 'language': 'English, French'},
#     'australia': {'capital': 'Canberra', 'language': 'English'},
#     'germany': {'capital': 'Berlin', 'language': 'German'},
#     'spain': {'capital': 'Madrid', 'language': 'Spanish'},
#     'china': {'capital': 'Beijing', 'language': 'Mandarin'},
#     'japan': {'capital': 'Tokyo', 'language': 'Japanese'},
#     'brazil': {'capital': 'Brasília', 'language': 'Portuguese'},
#     'south korea': {'capital': 'Seoul', 'language': 'Korean'},
#     'mexico': {'capital': 'Mexico City', 'language': 'Spanish'},
#     'russia': {'capital': 'Moscow', 'language': 'Russian'},
#     'south africa': {'capital': 'Pretoria, Cape Town, Bloemfontein', 'language': 'Afrikaans, English, Zulu, Xhosa, Sotho, Tswana, Venda, Tsonga, Swazi, Ndebele'},
#     'argentina': {'capital': 'Buenos Aires', 'language': 'Spanish'},
#     'egypt': {'capital': 'Cairo', 'language': 'Arabic'},
#     'nigeria': {'capital': 'Abuja', 'language': 'English'},
#     'saudi arabia': {'capital': 'Riyadh', 'language': 'Arabic'},
#     'turkey': {'capital': 'Ankara', 'language': 'Turkish'},
#     'indonesia': {'capital': 'Jakarta', 'language': 'Indonesian'},
#     'thailand': {'capital': 'Bangkok', 'language': 'Thai'},
#     'sweden': {'capital': 'Stockholm', 'language': 'Swedish'},
#     'norway': {'capital': 'Oslo', 'language': 'Norwegian'},
#     'switzerland': {'capital': 'Bern', 'language': 'German, French, Italian, Romansh'},
#     'netherlands': {'capital': 'Amsterdam', 'language': 'Dutch'},
#     'belgium': {'capital': 'Brussels', 'language': 'Dutch, French, German'},
#     'portugal': {'capital': 'Lisbon', 'language': 'Portuguese'},
# }

# user_country = input("Enter the country name: ").lower()
# if user_country in countries:
#     country = countries[user_country]
#     print(f"Capital of {user_country} is {country['capital']}. They speak {country['language']}.")
# else:
#     print("Not Found")


'''
Question 2
Write python code that will create a dictionary containing key, value pairs
that represent the first 12 values of the Fibonacci sequence
i.e {1:0,2:1,3:1,4:2,5:3,6:5,7:8 etc}
'''
# fib = {}
# fib[1] = 0
# fib[2] = 1

# for i in range(3, 13):
#     fib[i] = fib[i-1] + fib[i-2]
    
# print(fib)
    

'''
Question 3
Create a dictionary to represent the open, high, low, close share price data
for 4 imaginary companies. 'Python DS', 'PythonSoft', 'Pythazon' and 'Pybook'
the 4 sets of data are [12.87, 13.23, 11.42, 13.10],[23.54,25.76,21.87,22.33],
[98.99,102.34,97.21,100.065],[203.63,207.54,202.43,205.24]
'''
# stock_data = {
#     'Python DS': {'Open': 12.87, 'High': 13.23, 'Low': 11.42, 'Close': 13.10},
#     'PythonSoft': {'Open': 23.54, 'High': 25.76, 'Low': 21.87, 'Close': 22.33},
#     'Pythazon': {'Open': 98.99, 'High': 102.34, 'Low': 97.21, 'Close': 100.065},
#     'Pybook': {'Open': 203.63, 'High': 207.54, 'Low': 202.43, 'Close': 205.24}
# }

# print(stock_data['Python DS']['High'])


'''
Question 4
Go to the python module web page and find a module that you like. Play with it,
read the documentation and try to implement it.
'''
import webbrowser as wb
# wb.open("https://docs.python.org/3/library/webbrowser.html")

'''
Question 5
Create a dictoinary containing as keys the letters from A-Z, the values should
be random numbers created from the random module. Can you draw a bar graph of
the results?
'''
# from random import randint
# import matplotlib.pyplot as pp
# dist = {}
# for c in range(65, 91):
#     dist[chr(c)] = randint(1, 1000)
    
# x, y = zip(*dist.items())

# pp.bar(x, y)

'''
Question 6
Create a dictionary containing 4 suits of 13 cards
['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
'''
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']

cards = {f'{v} of {k}': {"Suit": k, "Rank": v } for k in suits for v in ranks}

print(cards)