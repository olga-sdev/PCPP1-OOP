"""
Inheriting properties from built-in classes
Python gives you the ability to create a class that inherits properties from any Python built-in class in order to get
a new class that can enrich the parent's attributes or methods.
As a result, your newly-created class has the advantage of all of the well-known functionalities inherited from its
parent or even parents and you can still access those attributes and methods.

Python allows you to subclass any built-in class such as a list, tuple, dictionary, and many others;
by subclassing the built-ins, you can easily adapt generics to provide more sophisticated features;
by subclassing the built-ins, you can modify only the parts (methods, attributes) that you intend to modify,
 while all remaining parts will behave as good old built-ins.
"""


# Example 1: Lists
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


# Example 2 - Dictionaries
from datetime import datetime


class DictionaryMonitorUpdates(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.log = list()
        self.logging_time('DictionaryMonitorUpdates created')

    def update(self, __m, **kwargs):
        super().update(__m)
        self.logging_time(f'dictionary {__m} updated')

    def logging_time(self, notification):
        log_time = datetime.now().strftime("%Y-%m-%d (%H:%M:%S.%f)")
        self.log.append(f'{log_time}: {notification}')


monitor = DictionaryMonitorUpdates()
monitor['model'] = 'Oppo'

monitor.update({'memory': 128})
print(f'Monitor: {monitor}')
print('\n'.join(monitor.log))


# Monitor: {'model': 'Oppo', 'memory': 128}
# 2025-01-16 (02:33:51.007759): DictionaryMonitorUpdates created
# 2025-01-16 (02:33:51.007759): dictionary {'memory': 128} updated


