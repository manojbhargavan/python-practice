# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 13:04:32 2024

@author: manoj
"""

class Patient(object):
    
    status = "In Patient"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.conditions = []
        
    def get_details(self) -> str:
        return f"Name: {self.name}, Age: {self.age}, Status: {self.status}, Conditions: {self.conditions}"
    
    def add_condition(self, condition: str):
        self.conditions.append(condition)
    
ram = Patient('Ram', 30)
print(ram.get_details())
ram.add_condition("Back Pain")
ram.add_condition("Headache")
print(ram.get_details())

jam = Patient('Jam', 30)
ram.status = 'Out Patient'
print(ram.get_details())
print(jam.get_details())