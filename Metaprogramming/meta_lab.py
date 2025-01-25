"""
Objectives
improving the student's skills in operating with metaclasses;
improving the student's skills in operating with class variables and class methods.

Scenario
Imagine you’ve been given a task to clean up the code of a system developed in Python – the code should be treated as legacy code;
the system was created by a group of volunteers who worked with no clear “clean coding” rules;
the system suffers from a problem: we don’t know in which order the classes are created, so it causes multiple dependency problems;

your task is to prepare a metaclass that is responsible for:
equipping all newly instantiated classes with time stamps, persisted in a class attribute named instantiation_time;
equipping all newly instantiated classes with the get_instantiation_time() method. The method should return the value of the class attribute instantiation_time.
* The metaclass should have its own class variable (a list) that contains a list of the names of the classes instantiated by the metaclass
(tip: append the class name in the __new__ method).

Your metaclass should be used to create a few distinct legacy classes;
create objects based on the classes;
list the class names that are instantiated by your metaclass.
"""

import time


def get_instantiation_time(self):
    return time.time()


class My_Meta(type):
    def __new__(mcs, name, bases, dictionary):
        if 'instantiation_time' not in dictionary:
            dictionary['instantiation_time'] = get_instantiation_time
        obj = super().__new__(mcs, name, bases, dictionary)
        return obj

class Medical_Order(metaclass=My_Meta):
    pass

class Grocery_Order(metaclass=My_Meta):
    def get_instantiation_time(self):
        return time.time()


# metaclasses can control the process of class instantiation, and adjust created classes to conform with selected rules:
med = Medical_Order()
print(med.instantiation_time())
groc = Grocery_Order()
print(groc.get_instantiation_time())
