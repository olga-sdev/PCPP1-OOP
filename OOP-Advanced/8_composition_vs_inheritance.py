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
"""


class Laptop:
    def __init__(self, memory):
        self.memory = memory


class RAM:
    def __init__(self, capacity):
        self.capacity = capacity

    def add_memory(self):
        print(f'The Laptop RAM capacity is {self.capacity} GB')


class Storage:
    def __init__(self, capacity):
        self.capacity = capacity

    def add_memory(self):
        print(f'The Laptop Storage capacity is {self.capacity} TB')


super_laptop = Laptop(RAM(32))
super_laptop.memory.add_memory()
super_laptop.memory = Storage(1)
super_laptop.memory.add_memory()

# The Laptop RAM capacity is 32 GB
# The Laptop Storage capacity is 1 GB/TB
