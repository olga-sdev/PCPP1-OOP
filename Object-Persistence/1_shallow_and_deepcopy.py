"""
Variables - fundamental elements that allow us to cope with objects.

An object my_list is created in the computer's memory -> has its identity;
The object is populated with other objects -> has a value;
A variable (label or name binding) is created -> distinct place in the computer memory.

The built-in id() function returns the 'identity' of an object -> address of the object in the memory.
This is an integer which is guaranteed to be UNIQUE and constant for this object during its lifetime.
Two objects with non-overlapping lifetimes MAY have the SAME id() value.

If 2 vars referring to the same object -> id() function is the same.

'==' -> value equality
'is' -> identity equality

list[:] is a handy trick to create a shallow copy of a list:
list[:] slices the entire list from start to end, creating a new list with the same elements as the original one.
To make an independent copy of a compound object (list, dictionary, custom class instance) -> use of deepcopy()

3 ways of copying a large compound object:
* simple reference copy;
* shallow copy -> slower than the previous code
* deep copy-> most comprehensive operation
"""

my_list_1 = ['Data', None, 1]
my_list_2 = ['Data', None, 1]
my_list_3 = my_list_2

print(f'id of my_list_1 is {id(my_list_1)}')
print(f'id of my_list_2 is {id(my_list_2)}')
print(f'id of my_list_3 is {id(my_list_3)}')
print(f'values for lists are equal: {my_list_1 == my_list_2}')
print(f'identities for lists are equal: {my_list_2 == my_list_3}')

# id of my_list_1 is 1841391255936
# id of my_list_2 is 1841391211072
# id of my_list_3 is 1841391211072
# values for lists are equal: True
# identities for lists are equal: True


# shallow copy
list_of_numbers = [[1], 3, [2]]
shallow_list = list_of_numbers[:]
print(list_of_numbers, id(list_of_numbers))  # [[1], 3, 2] 2183105045760
print(shallow_list, id(shallow_list))  # [[1], 3, 2] 2183104910272

shallow_list[0] = 0
print(list_of_numbers)  # [[1], 3, [2]] does not affect the original list
print(shallow_list)  # [0, 3, [2]] affects the copied list

shallow_list[2][0] = 10
print(list_of_numbers)  # [[1], 3, [10]] - affects the original list
print(shallow_list)  # [0, 3, [10]] - affects the copied list


# deep copy -> deepcopy() method
import copy


list_of_numbers = [[1], 3, [2]]
deep_list = copy.deepcopy(list_of_numbers)
print(list_of_numbers, id(list_of_numbers))  # [[1], 3, 2] 2183105045760
print(deep_list, id(deep_list))  # [[1], 3, 2] 2183104910272

deep_list[0] = 0
print(list_of_numbers)  # [[1], 3, [2]] does not affect the original list
print(deep_list)  # [0, 3, [2]] affects the copied list

deep_list[2][0] = 10
print(list_of_numbers)  # [[1], 3, [2]] - does not affect the original list
print(deep_list)  # [0, 3, [10]] - affects the copied list


# deepcopy() for dictionary

import copy

music_band_dict = {
    'name': 'Kaleo',
    'songs': ['Save Yourself', 'Automobile']
    }
copied_band_dict = copy.deepcopy(music_band_dict)
print('Memory chunks:', id(music_band_dict), id(copied_band_dict))
print('Same memory chunk?', music_band_dict is copied_band_dict)
print("Let's modify the list")
music_band_dict['songs'].append('Vor i Vaglaskogi')
print(music_band_dict['songs'])
print(copied_band_dict['songs'])

# Memory chunks: 140544517551440 140544516840256
# Same memory chunk? False
# Let's modify the list
# ['Save Yourself', 'Automobile', 'Vor i Vaglaskogi']
# ['Save Yourself', 'Automobile']


# example with cls

import copy


class Files:
    def __init__(self):
        self.format = ['pdf', 'docs', 'py', 'ods']


files = Files()
my_files = copy.deepcopy(files)
print('same memory chunk?', files is my_files)
my_files.format.pop()
print(files.format)
print(my_files.format)

# same memory chunk? False
# ['pdf', 'docs', 'py', 'ods']
# ['pdf', 'docs', 'py']
