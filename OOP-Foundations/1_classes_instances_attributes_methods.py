"""
In Python everything is an object (functions, modules, lists, etc.).

* class — an idea, blueprint, or recipe for an instance;
* instance — an instantiation of the class;
* object — Python's representation of data and methods;
* attribute — any object or class trait; could be a variable or method;
* method — a function built into a class that is executed on behalf of the class or object;
some say that it’s a 'callable attribute';
* type — refers to the class that was used to instantiate the object.
"""


class SmartPhone:
    '''
    Creating a Class with variables and methods
    '''
    def __init__(self, model, colour):
        self.model = model
        self.colour = colour

    def communicate(self):
        print("Call, Text, Emails")

    def making_photo(self):
        print("Make photo")

    def play_media(self):
        print("Play Media")


# Creating an instance of the Class SmartPhone
samsung = SmartPhone("Samsung Galaxy S25 Ultra", "White")
oneplus = SmartPhone("OnePlus Open 2", "Green")
apple = SmartPhone("Apple iPhone 17", "Blue")

# Call method
samsung.communicate() # Call, Text, Emails

# access attribute
print(samsung.model) # Samsung Galaxy S25 Ultra

# types of object
print(SmartPhone.__class__) # <class 'type'>
print(oneplus.__class__) # <class '__main__.SmartPhone'>
print(oneplus.model.__class__) # <class 'str'>
print(oneplus.communicate.__class__) # <class 'method'>
