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


# deep copy

