"""
Abstract class is a blueprint for other classes - contract between a class designer and a programmer.

Class designer sets requirements regarding methods that must be implemented by just declaring them.
An abstract method is a method that has a declaration, but does not have any implementation.

The programmer delivers the method definitions by overriding the method declarations received from the class designer.

This contract assures you that a child cls will be equipped with a set of concrete methods imposed by the abstract cls.

Python has a module which provides the helper class for defining Abstract Base Classes (ABC) -> abc.
"""

import abc
from datetime import datetime


class Clock(abc.ABC):
    @abc.abstractmethod
    def show_time(self):
        pass


class ChimingClock(Clock):
    def show_time(self):
        print(datetime.now().strftime('%H:%M:%S'))


class AlarmClock(Clock):
    def alarming(self):
        pass


ChimingClock().show_time()
AlarmClock().alarming()

# 23:17:12
# TypeError: Can't instantiate abstract class AlarmClock without an implementation for abstract method 'show_time'
