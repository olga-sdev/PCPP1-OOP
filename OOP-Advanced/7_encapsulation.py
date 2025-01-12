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


class Freezer:
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
                raise TemperatureError('Too minimum level of temperature for freezer')
        elif temperature > 0:
            raise TemperatureError('Impossible to set high level temperature for freezer')

    @level.deleter
    def level(self):
        if self.__level > 0:
            print('Recommend to switch off the freezer')
        self.__level = None


# the fridge temperature has minimum level -18
freezer = Freezer(-18)

# set the current level of freezer
freezer.level = -12

# change the level for freezer - colder for 1°C
freezer.level -= 1

# set the level for freezer above 0 - it raises an error, cause there is no sense in freezer
try:
    freezer.level = 1
except TemperatureError as tmp_err:
    print('Trying to set the level for freezer above 0 that cause: ', tmp_err)

# set the level for freezer that is does not support
try:
    freezer.level = -19
except TemperatureError as tmp_err:
    print('Trying to set the level for freezer that it does not support')

print(f'Current temperature for freezer is: {freezer.level}')

del freezer.level

print(f'Current temperature for freezer after cleanup is: {freezer.level}')

# Trying to set the level for freezer above 0 that cause:  Impossible to set high level temperature for freezer
# Trying to set the level for freezer that it does not support
# Current temperature for freezer is: -13
# Current temperature for freezer after cleanup is: None
