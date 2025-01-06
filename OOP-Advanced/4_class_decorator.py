"""
In Python, decorator can be a class or function.

Decorator in class is implemented with a help of __call__ special class method.

Classes bring all the subsidiarity they can offer, like inheritance and the ability to create dedicated methods.
"""

# Example 1 - Decorator Class
from datetime import datetime


class TimeDecor:
    def __init__(self, own_function):
        # the __init__ method assigns a decorated function reference to the self.attribute for later use
        self.own_function = own_function

    def __call__(self, hour):
        """
        the __call__ method calls a previously referenced function
        :param hour: arg that is used in decorated function
        """
        today = datetime.now().strftime("%Y-%m-%d %H:%M")
        print(f'Time is "{today}"')
        self.own_function(hour)


@TimeDecor
def say_hello(hour):
    if 0 <= hour < 6:
        print('Good night!')
    elif 6 <= hour < 12:
        print('Good morning!')
    elif 12 <= hour < 18:
        print('Good afternoon!')
    elif 18 <= hour < 24:
        print('Good evening!')


hour_now = datetime.now().hour
say_hello(hour_now)

# Time is "2025-01-06 21:21"
# Good evening!


# Example 2 - Decorator with own args
class MonthDecorator:
    def __init__(self, month):
        self.month = month

    def __call__(self, function):
        """
        the decorator arguments are passed to __init__ method
        :param function: is a decorated function
        """
        def internal_wrapper(hour):
            today = datetime.now().strftime("%Y-%m-%d %H:%M")
            print(f'Today is "{self.month}: {today}"')
            function(hour)
        return internal_wrapper


month_name = datetime.now().strftime("%B")


@MonthDecorator(month_name)
def say_hello(hour):
    if 0 <= hour < 6:
        print('Good night!')
    elif 6 <= hour < 12:
        print('Good morning!')
    elif 12 <= hour < 18:
        print('Good afternoon!')
    elif 18 <= hour < 24:
        print('Good evening!')


hour_now = datetime.now().hour
say_hello(hour_now)

# Today is "January: 2025-01-06 21:30"
# Good evening!
