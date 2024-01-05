# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 11:45:32 2023

@author: manoj
"""

# Dict

capitals = {
        'India': 'Delhi', 'Spain': 'Madrid', 'USA': 'Washington DC'
    }

print(capitals['India'])
print(capitals.get('India'))
capitals['Germany'] = 'Berlin'
print(capitals)

for country, capital in capitals.items():
    print(f"The capital of {country} is {capital}")
    
print('India' in capitals)
print('UK' in capitals)