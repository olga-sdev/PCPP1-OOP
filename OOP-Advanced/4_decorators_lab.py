"""
Objectives
Improving the student's skills in creating decorators and operating with them.

Scenario
Create a function decorator that prints a timestamp (in a form like year-month-day hour:minute:seconds, eg. 2019-11-05 08:33:22)
Create a few ordinary functions that do some simple tasks, like adding or multiplying two numbers.
Apply your decorator to those functions to ensure that the time of the function executions can be monitored.
"""

from datetime import datetime


def timestamp_decor(function):
    def wrapper(*args):
        now = datetime.now()
        time_now = now.strftime('%Y-%m-%d %H:%M:%S')
        print(time_now)
        function(*args)

    return wrapper


@timestamp_decor
def add_nums(a, b):
    print(a + b)


@timestamp_decor
def mul_nums(a, b):
    print(a * b)


day = datetime.now().day
week = 7
age = 37
days_in_year = 365

add_nums(day, week)
mul_nums(age, days_in_year)

# 2025-01-06 20:38:42
# 13
# 2025-01-06 20:38:42
# 13505

