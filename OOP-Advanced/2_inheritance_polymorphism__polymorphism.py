"""
One way to carry out polymorphism is inheritance, when subclasses make use of base class methods, or override them.

Polymorphism:
* is used when different class objects share conceptually similar methods (but are not always inherited);
* leverages clarity and expressiveness of the application design and development;
* when polymorphism is assumed, it is wise to handle exceptions that could pop up.
"""


class Device:
    def turn_on(self):
        print('The device was turned on')


class Mp3Player(Device):
    pass


class SmartPhone(Device):
    def turn_on(self):
        print('SmartPhone type object was turned on')


class Faucet:
    def turn_on(self):
        print('Faucet type object was turned on')


class Plane:
    def take_off(self):
        print('Plane type object was taken off')


device = Device()  # The device was turned on
mp3player = Mp3Player()  # The device was turned on
smartPhone = SmartPhone()  # SmartPhone type object was turned on
faucet = Faucet()  # Faucet type object was turned on
plane = Plane()  # No turn_on() method

for element in (device, mp3player, smartPhone, faucet, plane):
    try:
        element.turn_on()
    except AttributeError:
        print('No turn_on() method')
