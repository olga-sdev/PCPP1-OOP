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


# Example with the Class and methods
class ProjectRole:
    def __init__(self, salary, bonus):
        self.salary = salary
        self.bonus = bonus

    def __add__(self, other):
        return self.salary + other.salary

    def __str__(self):
        return str(self.salary)

    @staticmethod
    def sum_total_salaries(*args):
        total_project_cost = sum(arg.salary for arg in args)
        return total_project_cost


dev = ProjectRole(105, 10)
po = ProjectRole(110, 7)
sm = ProjectRole(90, 5)

print(ProjectRole.sum_total_salaries(dev, po, sm))
