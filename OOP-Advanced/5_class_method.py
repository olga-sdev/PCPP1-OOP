"""
Class methods are methods that are bound to the class and not the instance of the class:

* cls method is defined using the @classmethod decorator;
* cls method updates the class variable, which is shared across all instances of the class;
* instance method operates on individual instance variables.

Cls methods are useful for development of utility methods that operate on cls itself rather than on individual instances
"""


# Example 1 - Class Methods
class MyClass:
    class_var = 'class_var'

    def __init__(self, instance_var):
        self.instance_var = instance_var

    @classmethod
    def class_method(cls):
        print(cls.class_var)

    def instance_method(self):
        print(self.instance_var)


my_class_1 = MyClass('instance_var_1')
my_class_2 = MyClass('instance_var_2')

my_class_1.class_method()
my_class_2.class_method()

my_class_1.instance_method()
my_class_2.instance_method()

# class_var
# class_var
# instance_var_1
# instance_var_2
