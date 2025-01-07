"""
Static methods do not require a param indicating the class object or the class itself in order to execute their code:

* utility method is semantically related to class, but does not require an object of that class to execute its code;
* static method does not need to know the state of the objects or classes (perform a task in isolation).
"""


class CheckInputValue:
    def __init__(self, input_value):
        self.input_value = input_value

    @staticmethod
    def validate_input_value(value):
        if isinstance(value, bool):
            print(f'The input value "{value}" is a boolean')
        else:
            print(f'The value "{value}" is not a boolean. It is "{type(value)}"')


values = ('number', 365, 365.0, True)

[CheckInputValue.validate_input_value(value) for value in values]


# The value "number" is not a boolean. It is "<class 'str'>"
# The value "365" is not a boolean. It is "<class 'int'>"
# The value "365.0" is not a boolean. It is "<class 'float'>"
# The input value "True" is a boolean
