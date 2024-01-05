# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 15:17:56 2019

@author: giles
"""

'''
Question 1

Create a class to represent a bank account. It will need to have a balance,
a method of withdrawing money, depositing money and displaying the balance to
the screen. Create an instance of the bank account and check that the methods
work as expected.
'''
class BankAccount(object):
    
    def __init__(self, holder_name, balance):
        self.holder_name = holder_name
        self.balance = balance
        
    def withdraw(self, amount):
        if(self.balance >= amount):
            self.balance -= amount
            return amount
        else:
            return 0
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.balance
        else:
            return self.balance
        
    def display_balance(self):
        print(f"Holder: {self.holder_name}, Account Balance: {self.balance}.")
        
raj = BankAccount('Raj', 20)
raj.deposit(100)
raj.withdraw(30)
raj.display_balance()


'''
Question 2
 Create a circle class that will take the value of a radius and
 return the area of the circle
'''
import math
class Circle(object):
    
    def __init__(self, radius):
        self.radius = radius
        
    def get_area(self):
        return round(math.pi * self.radius ** 2, 5)
    
mycir = Circle(8)
print(mycir.get_area())