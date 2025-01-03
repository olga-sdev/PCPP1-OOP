"""
Python core syntax – an ability to perform specific operations on different data types, when operations are formulated using the same operators or instructions, or even functions.

Python core syntax covers:

operators like '+', '-', '*', '/', '%' and many others;
operators like '==', '<', '>', '<=', 'in' and many others;
indexing, slicing, subscripting;
built-in functions like str(), len()
reflexion – isinstance(), issubclass()
and a few more elements.

Comparison methods
Function or operator	Magic method	Implementation meaning or purpose
==	__eq__(self, other)	equality operator
!=	__ne__(self, other)	inequality operator
<	__lt__(self, other)	less-than operator
>	__gt__(self, other)	greater-than operator
<=	__le__(self, other)	less-than-or-equal-to operator
>=	__ge__(self, other)	greater-than-or-equal-to operator

Numeric methods
Unary operators and functions
Function or operator	Magic method	Implementation meaning or purpose
+	__pos__(self)	unary positive, like a = +b
-	__neg__(self)	unary negative, like a = -b
abs()	__abs__(self)	behavior for abs() function
round(a, b)	__round__(self, b)	behavior for round() function

Common, binary operators and functions
Function or operator	Magic method	Implementation meaning or purpose
+	__add__(self, other)	addition operator
-	__sub__(self, other)	subtraction operator
*	__mul__(self, other)	multiplication operator
//	__floordiv__(self, other)	integer division operator
/	__div__(self, other)	division operator
%	__mod__(self, other)	modulo operator
**	__pow__(self, other)	exponential (power) operator

Augumented operators and functions
By augumented assignment we should understand a sequence of unary operators and assignments like a += 20

Function or operator	Magic method	Implementation meaning or purpose
+=	__iadd__(self, other)	addition and assignment operator
-=	__isub__(self, other)	subtraction and assignment operator
*=	__imul__(self, other)	multiplication and assignment operator
//=	__ifloordiv__(self, other)	integer division and assignment operator
/=	__idiv__(self, other)	division and assignment operator
%=	__imod__(self, other)	modulo and assignment operator
**=	__ipow__(self, other)	exponential (power) and assignment operator
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
