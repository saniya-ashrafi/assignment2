# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 12:27:27 2020

@author: DELL
"""

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seatcap(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Bus(Vehicle):
    def seatcap(self, capacity=50):
        return super().seatcap(capacity=50)

School_bus = Bus("School Volvo", 180, 12)
print(School_bus.seatcap())