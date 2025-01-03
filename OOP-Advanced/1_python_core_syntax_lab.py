"""
Objectives
improving the student's skills in operating with special methods

Scenario
Create a class representing a time interval;
the class should implement its own method for addition, subtraction on time interval class objects;
the class should implement its own method for multiplication of time interval class objects by an integer-type value;
the __init__ method should be based on keywords to allow accurate and convenient object initialization,
but limit it to hours, minutes, and seconds parameters;
the __str__ method should return an HH:MM:SS string, where HH represents hours, MM represents minutes and
SS represents the seconds attributes of the time interval object;
check the argument type, and in case of a mismatch, raise a TypeError exception.


just before doing the math, convert each time interval to a corresponding number of seconds to simplify the algorithm;
for addition and subtraction, you can use one internal method, as subtraction is just ... negative addition.

Test data:

the first time interval (fti) is hours=21, minutes=58, seconds=50
the second time interval (sti) is hours=1, minutes=45, seconds=22
the expected result of addition (fti + sti) is 23:44:12
the expected result of subtraction (fti - sti) is 20:13:28
the expected result of multiplication (fti * 2) is 43:57:40

you can use the assert statement to validate if the output of the __str__ method
applied to a time interval object equals the expected value.

Scenario
Extend the class implementation prepared in the previous lab to support the addition and subtraction of integers
to time interval objects;
to add an integer to a time interval object means to add seconds;
to subtract an integer from a time interval object means to remove seconds.

in the case when a special method receives an integer type argument, instead of a time interval object, create a new time interval object based on the integer value.
Test data:

the time interval (tti) is hours=21, minutes=58, seconds=50
the expected result of addition (tti + 62) is 21:59:52
the expected result of subtraction (tti - 62) is 21:57:48
"""


class TimeInterval:

    def __init__(self, hour, minute, second):
        if not isinstance(hour, int) or not isinstance(minute, int) or not isinstance(second, int):
            raise TypeError
        self.hour = hour
        self.minute = minute
        self.second = second

    def convert_time_to_seconds(self):
        total_seconds = self.hour * 3600 + self.minute * 60 + self.second
        return total_seconds

    @staticmethod
    def convert_seconds_to_time(seconds):
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        remaining_seconds = seconds % 60
        return hours, minutes, remaining_seconds

    def __add__(self, other):
        if isinstance(other, TimeInterval):
            sum_seconds = self.convert_time_to_seconds() + other.convert_time_to_seconds()
        elif isinstance(other, int):
            sum_seconds = self.convert_time_to_seconds() + other
        else:
            raise TypeError
        calc_time = self.convert_seconds_to_time(sum_seconds)
        calc_time_str = f'{calc_time[0]}:{calc_time[1]}:{calc_time[2]}'
        return calc_time_str

    def __sub__(self, other):
        if isinstance(other, TimeInterval):
            sub_seconds = self.convert_time_to_seconds() - other.convert_time_to_seconds()
        elif isinstance(other, int):
            sub_seconds = self.convert_time_to_seconds() - other
        else:
            raise TypeError
        calc_time = self.convert_seconds_to_time(sub_seconds)
        calc_time_str = f'{calc_time[0]}:{calc_time[1]}:{calc_time[2]}'
        return calc_time_str

    def __mul__(self, num):
        if isinstance(num, int):
            mul_seconds = self.convert_time_to_seconds() * num
        else:
            raise TypeError
        calc_time = self.convert_seconds_to_time(mul_seconds)
        calc_time_str = f'{calc_time[0]}:{calc_time[1]}:{calc_time[2]}'
        return calc_time_str

    def __str__(self):
        time = f'{str(self.hour)}:{str(self.minute)}:{str(self.second)}'
        return time


fti = TimeInterval(21, 58, 50)
sti = TimeInterval(1, 45, 22)
print(fti + sti)
print(fti - sti)
print(fti * 2)
tti = TimeInterval(21, 58, 50)
print(tti + 62)
print(tti - 62)
