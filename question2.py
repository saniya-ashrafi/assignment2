# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 12:11:05 2020

@author: DELL
"""

n = 182; 
rev = 0
  
while(n > 0): 
    a = n % 10
    rev = rev * 10 + a 
    n = n // 10
      
print(rev) 
  