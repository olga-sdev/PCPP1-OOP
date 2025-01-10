"""
Encapsulation describes the idea of bundling attributes and methods that work on those attributes within a class.
Encapsulation is used to hide the attributes inside a class like in a capsule, preventing unauthorized parties' direct access to them.
Direct access to the object attribute should not be possible, but you can always invoke methods, acting like proxies.
Python introduces the concept of properties that act like proxies to encapsulated attributes.

Python allows to control access to attributes with built-in property() function and corresponding decorator @property:

it designates method which will be called automatically when another object wants to read encapsulated attribute value;
the name of designated method will be used as name of instance attribute corresponding to encapsulated attribute;
it should be defined before the method responsible for setting the value of the encapsulated attribute,
and before the method responsible for deleting the encapsulated attribute.
"""


class TemperatureError(Exception):
    pass


class Temperature:
    def __init__(self, minimum):
        self.minimum = minimum
        self.__level = 0

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, temperature):
        if temperature <= 0:
            if temperature >= self.minimum:
                self.__level = temperature
            else:
                raise TemperatureError('Too high level of temperature')
        elif temperature > 0:
            raise TemperatureError('Impossible to set high level temperature for fridge')

    @level.deleter
    def level(self):
        if self.__level > 0:
            print('Recommend to switch off the fridge')
        self.__level = None
