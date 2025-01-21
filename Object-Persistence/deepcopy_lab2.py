"""
Objectives
improving the student's skills in creating classes representing candies;
improving the student's skills in operating with deepcopy() and copy.

Scenario
The previous task was a very easy one. Now let's rework the code a bit:

introduce the Delicacy class to represent a generic delicacy.
The objects of this class will replace the old school dictionaries. Suggested attribute names: name, price, weight;
your class should implement the __str__() method to represent each object state;
experiment with the copy.copy() and deepcopy.copy() methods to see the difference in how each method copies objects .
"""


import copy


class Delicacy:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def __str__(self):
        return f'{self.name}, {self.price}, {self.weight}'


deli = Delicacy('deli', 999, 123)
print(deli, f'id of deli: {id(deli)}')

copy_deli = copy.copy(deli)
print(copy_deli, f'id of copy_deli: {id(copy_deli)}')

deepcopy_deli = copy.deepcopy(deli)
print(deepcopy_deli, f'id of deepcopy_deli: {id(deepcopy_deli)}')

deli.name = 'delicacy'  # change in original only
copy_deli.weight = 1  # changed in copy only
deepcopy_deli.price = 777777  # changed in deepcopy only

print(f'deli: {deli}', f'\ncopy_deli: {copy_deli}', f'\ndeepcopy_deli: {deepcopy_deli}')

# deli, 999, 123 id of deli: 139759234481552
# deli, 999, 123 id of copy_deli: 139759234574544
# deli, 999, 123 id of deepcopy_deli: 139759234505488
# deli: delicacy, 999, 123 
# copy_deli: deli, 999, 1 
# deepcopy_deli: deli, 777777, 123
