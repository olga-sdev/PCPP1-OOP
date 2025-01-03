"""
Class variables are defined in the class construction.
Available before class instance is created.
Get access to a class variable -> with the class name, then provide the variable name.

Class var stores metadata relevant to the class:

* fixed information like description, configuration, or identification values;
* mutable info like the number of instances created.
"""


class Application:
    class_var = 'class variable'


app = Application()

print(Application.class_var)  # class variable
print(app.class_var)  # class variable
print('content of app:', app.__dict__)  # content of app: {}


app.class_var = 'changed class var'
print(app.class_var)  # changed class var
