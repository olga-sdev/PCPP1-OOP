"""
Inheritance and polymorphism — Inheritance is a pillar of OOP

Inheritance expresses the fundamental relationships between classes:
superclasses (parents) and their subclasses (descendants).
Inheritance is a way of building a new class by using an already defined parameters and methods.

Each superclass is more general (more abstract) than any of its subclasses.

MRO — Method Resolution Order and Multiple inheritance

In the multiple inheritance scenario, any specified attribute is searched for first in the current class.
If it is not found, the search continues into the direct parent classes in depth-first level (the first level above),
from the left to the right, according to the class definition. This is the result of the MRO algorithm.
Classes can behave totally differently, because the order of the superclasses in derived class is different.
"""


class Vehicle:
    def info(self):
        print('Class Vehicle')


class Bicycle(Vehicle):
    def info(self):
        print('Class Bicycle')


class Plane(Vehicle):
    def info(self):
        print('Class Plane')


class AirBicycle(Bicycle, Plane):
    pass


class FlyBicycle(Plane, Bicycle):
    pass


AirBicycle().info()  # Class Bicycle
FlyBicycle().info()  # Class Plane
