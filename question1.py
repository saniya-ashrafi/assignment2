# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 12:10:15 2020

@author: DELL
"""

def mulsum(num1, num2):
    product = num1 * num2
    if product <= 1000:
        return product
    else:
        return num1 + num2

number1 = 20
number2 = 30

print("\n")
result = mulsum(number1, number2)
print("The result is", result)

