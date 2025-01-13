"""
Inheritance models is called an IS a relation.
Examples:
a Laptop is a (specialized form of) Computer;
a Square is a (specialized form of) Figure;
a Hovercraft is a Vehicle.

The primary use of inheritance is to reuse the code by transfer identical methods and properties from base to subclass.

Inheritance (especially multiple inheritances) creates a complex structure of classes
which would be hard to understand, debug, extend -> it's called a cls explosion problem (antipatterns of programming)

Composition models is called a HAS a relation.
Examples:
a Laptop has a network card;
a Hovercraft has a specific engine.


You should always examine the problem your code is about to solve before you start coding.
If the problem can be modeled using an “is a” relation, then the inheritance approach should be implemented.

Otherwise, if the problem can be modeled using a “has a” relation, then the choice is clear – composition is the solution.
"""


class Computer:
    def __init__(self, serial_number):
        self.serial_number = serial_number


class Laptop(Computer):
    def __init__(self, serial_number, memory):
        super().__init__(serial_number)
        print(f'Generated computer with SN {self.serial_number}')
        self.memory = memory


class Memory:
    def __init__(self, capacity):
        self.capacity = capacity

    def add_memory(self):
        pass


class RAM(Memory):
    def __init__(self, capacity):
        super().__init__(capacity)

    def add_memory(self):
        print(f'The Laptop RAM capacity is {self.capacity} GB')


class Storage(Memory):
    def __init__(self, capacity):
        super().__init__(capacity)

    def add_memory(self):
        print(f'The Laptop Storage capacity is {self.capacity} TB')


super_laptop = Laptop('FC4IC-5FMAA-1SAQZ-9W8Y1-JB95H', RAM(32))
super_laptop.memory.add_memory()
super_laptop.memory = Storage(1)
super_laptop.memory.add_memory()

# Generated computer with SN FC4IC-5FMAA-1SAQZ-9W8Y1-JB95H
# The Laptop RAM capacity is 32 GB
# The Laptop Storage capacity is 1 TB
