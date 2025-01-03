"""
Python core syntax – an ability to perform specific operations on different data types, when operations are formulated using the same operators or instructions, or even functions.

Python core syntax covers:

operators like '+', '-', '*', '/', '%' and many others;
operators like '==', '<', '>', '<=', 'in' and many others;
indexing, slicing, subscripting;
built-in functions like str(), len()
reflexion – isinstance(), issubclass()
and a few more elements.
"""


# The '+' operator is in fact converted to the __add__() magic method
number_20 = 20
number_18 = 18

statement = 'number_20 + number_18 == number_20.__add__(number_18)'

if number_20 + number_18 == number_20.__add__(number_18):
    print(f'Statement "{statement}" is True')
else:
    print(f'Statement "{statement}" is False')


# The len() function is converted to the __len__() magic method
statement = "len('Python') == 'Python'.__len__()"

if len('Python') == 'Python'.__len__():
    print(f'Statement "{statement}" is True')
else:
    print(f'Statement "{statement}" is False')
