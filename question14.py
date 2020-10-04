# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 13:05:58 2020

@author: DELL
"""
class IOString():
    def __init__(self):
        self.str1 = ""

    def get_String(self):
        self.str1 = input("enter the string:")

    def print_String(self):
        print(self.str1.upper("output:"))

str1 = IOString()
str1.get_String()
str1.print_String()