# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 13:05:58 2020

@author: DELL
"""

class InputOutString:
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input("enter the string:")

    def printString(self):
        print(self.s.upper())

strObj = InputOutString()
strObj.getString()
strObj.printString()

