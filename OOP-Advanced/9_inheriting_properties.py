"""
Inheriting properties from built-in classes
Python gives you the ability to create a class that inherits properties from any Python built-in class in order to get
a new class that can enrich the parent's attributes or methods.
As a result, your newly-created class has the advantage of all of the well-known functionalities inherited from its
parent or even parents and you can still access those attributes and methods.
"""


class RemoveDataStructures(list):

    @staticmethod
    def check_value_type(value):
        if not isinstance(value, list) and not isinstance(value, dict) and not isinstance(value, tuple):
            raise ValueError('Not a boolean type')

    def remove(self, value):
        RemoveDataStructures.check_value_type(value)
        list.remove(self, value)


list_of_values = RemoveDataStructures()
list_of_values.append(1)
list_of_values.append('a')
list_of_values.append(['1', '2', '3'])
list_of_values.append('b')
list_of_values.append(False)
list_of_values.append({'key': 'value'})
list_of_values.append((1, 2, 3))

print(f'The initial list: {list_of_values}')

for item in list_of_values[:]:
    try:
        list_of_values.remove(item)
    except ValueError as val_err:
        print(f'The {item} is a {type(item)}')


print(f'The updated list: {list_of_values}')

# [1, 'a', ['1', '2', '3'], 'b', False, {'key': 'value'}, (1, 2, 3)]
# The 1 is a <class 'int'>
# The a is a <class 'str'>
# The b is a <class 'str'>
# The False is a <class 'bool'>
# [1, 'a', 'b', False]
