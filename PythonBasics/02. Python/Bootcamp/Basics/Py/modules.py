# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 11:12:22 2023

@author: manoj
"""

import math
import random
import webbrowser

print(math.pi)
print(math.sqrt(25))
print(math.cos(0))

print(random.randint(1, 1000))

for i in range(1, random.randint(1, 1000)):
    print(random.randint(1, 100), end=' ')
    
webbrowser.open("http://google.com")