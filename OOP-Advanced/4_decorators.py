"""
The decorator's operation is based on wrapping the original function with a new "decorating" function (or class).
Decorators are universal and support any function, regardless of number and type of arguments passed (*args **kwargs).
In Python, it's possible to create a decorator with oun args: @decorator(arg)

Decorators are used in:

the validation of arguments;
the modification of arguments;
the modification of returned objects;
the measurement of execution time;
message logging;
thread synchronization;
code refactoring;
caching.
"""

# Example 1 - Decorator and function
from datetime import datetime


def time_decorator(function):
    now = datetime.now()
    today = now.strftime("%Y-%m-%d %H:%M")
    print(f'Time is "{today}"')
    return function


@time_decorator
def simple_hello():
    print("Hello!")


simple_hello()


# Time is "2025-01-06 17:30"
# Hello!


# Example 2 - Decorator and function with arg
def time_decorator(own_function):
    def internal_wrapper(hour):
        now = datetime.now()
        today = now.strftime("%Y-%m-%d %H:%M")
        print(f'Time is "{today}"')
        own_function(hour)

    return internal_wrapper


@time_decorator
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


# Time is "2025-01-06 17:30"
# Good afternoon!


# Example 3 - Decorator with own arg
def month_decorator(month):
    def wrapper(function):
        def internal_wrapper(hour):
            now = datetime.now()
            today = now.strftime("%Y-%m-%d %H:%M")
            print(f'Today is "{month}: {today}"')
            function(hour)

        return internal_wrapper

    return wrapper


month_name = datetime.now().strftime("%B")


@month_decorator(month_name)
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

# Today is "January: 2025-01-06 17:57"
# Good afternoon!


# Example 4 - Double Decorator
def day_decorator(day):
    def wrapper(function):
        def internal_wrapper(hour):
            week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
            if day in week_days:
                print(f'Today is Weekday: "{day}"')
            else:
                print(f'Today is Holiday: "{day}"')
            function(hour)

        return internal_wrapper

    return wrapper


def month_decorator(month):
    def wrapper(function):
        def internal_wrapper(hour):
            now = datetime.now()
            today = now.strftime("%Y-%m-%d %H:%M")
            if month == 'January' or month == 'February' or month == 'December':
                print(f'Today is Winter: "{month} {today}"')
            elif month == 'March' or month == 'April' or month == 'May':
                print(f'Today is Spring: "{month} {today}"')
            elif month == 'June' or month == 'July' or month == 'August':
                print(f'Today is Summer: "{month} {today}"')
            elif month == 'September' or month == 'October' or month == 'November':
                print(f'Today is Autumn: "{month} {today}"')
            function(hour)

        return internal_wrapper

    return wrapper


now = datetime.now()
month_name = now.strftime("%B")
day_name = now.strftime("%A")


@month_decorator(month_name)
@day_decorator(day_name)
def say_hello(hour):
    if 0 <= hour < 6:
        print('Good night!')
    elif 6 <= hour < 12:
        print('Good morning!')
    elif 12 <= hour < 18:
        print('Good afternoon!')
    elif 18 <= hour < 24:
        print('Good evening!')


hour_now = now.hour
say_hello(hour_now)

# Today is Winter: "January 2025-01-06 20:19"
# Today is Weekday: "Monday"
# Good evening!
