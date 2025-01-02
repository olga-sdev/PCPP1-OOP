'''
Working with class and instance data – the LAB

Objectives:
creating classes, class and instance variables;
accessing class and instance variables.

Scenario
Imagine that you receive a task description of an application that monitors the process of apple packaging before
the apples are sent to a shop.

A shop owner has asked for 1000 apples, but the total weight limitation cannot exceed 300 units.

Write a code that creates objects representing apples as long as both limitations are met.
When any limitation is exceeded, then the packaging process is stopped,
and your application should print the number of apple class objects created, and the total weight.

Your application should keep track of two parameters:
the number of apples processed, stored as a class variable;
the total weight of the apples processed; stored as a class variable.
Assume that each apple's weight is random, and can vary between 0.2 and 0.5 of an imaginary weight unit;

Hint: Use a random.uniform(lower, upper) function to create a random number between the lower and upper float values.
'''

import random


class Apple:
    number_of_apples_processed = 0
    total_weight_of_apples = 0

    def pack_apples(self):
        while Apple.number_of_apples_processed <= 1000 or Apple.total_weight_of_apples <= 300:
            Apple.total_weight_of_apples += random.uniform(0.2, 0.5)
            Apple.number_of_apples_processed += 1
            if Apple.number_of_apples_processed >= 1000 or Apple.total_weight_of_apples >= 300:
                print(f'{Apple.number_of_apples_processed} apples and {Apple.total_weight_of_apples} kg')
                break


apple = Apple()
apple.pack_apples()
