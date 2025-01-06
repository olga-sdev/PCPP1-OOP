"""
In Python, decorators can be used to modify classes as well as functions.
Class decorator is a way to add functionality to class or modify its behavior without directly changing the class's code
"""
from datetime import datetime


# Example 1 - Decorated Class
def log_time_decor(cls):
    def add_time_method(self):
        return f'Logging time: {datetime.now()}'
    cls.add_time_method = add_time_method
    return cls


@log_time_decor
class MyClass:
    def __init__(self, name):
        self.name = name


my_class = MyClass('MyClass')
print(my_class.add_time_method())

# Logging time: 2025-01-06 22:22:14.601825


# Example 2 - Decorated class with args
def add_month_decor(month):
    def log_time_decor(cls):
        orig_str = cls.__str__
        def time_str(self):
            return f'Logging time for {orig_str(self)}: {datetime.now()} - its a {month}'
        cls.__str__ = time_str
        return cls
    return log_time_decor


month_name = datetime.now().strftime("%B")


@add_month_decor(month_name)
class MyClass:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


my_time_class = MyClass('My Time Class')
print(my_time_class)

# Logging time for My Time Class: 2025-01-06 22:40:49.505621 - its a January


# Example 3 - Diverse Decoration of the Class
def modify_str_decor(cls):
    orig_str = cls.__str__
    def modify(self):
        return orig_str(self).title()
    cls.__str__ = modify
    return cls


def add_month_decor(month):
    def log_time_decor(cls):
        orig_str = cls.__str__
        def time_str(self):
            return f'Logging time for {orig_str(self)}: {datetime.now()} - its a {month}'
        cls.__str__ = time_str
        return cls
    return log_time_decor


@add_month_decor(month_name)
@modify_str_decor
class MyClass:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


my_time_class = MyClass('my time class')
print(my_time_class)

# Logging time for My Time Class: 2025-01-06 23:29:38.129363 - its a January
