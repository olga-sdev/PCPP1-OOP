"""
Shelve module implements a serialization dictionary where objects are pickled and associated with a key:
* the keys must be strings;
* to enforce an immediate flush, call the sync() method on your shelve object;
* when you call the close() method on an shelve object, it also flushes the buffers.

When you treat a shelve object like a Python dictionary, you can make use of the dictionary utilities:
the len() function;
the in operator;
the keys() and items() methods;
the update operation, which works the same as when applied to a Python dictionary;
the del instruction, used to delete a key-value pair.


The meaning of the optional flag parameter:

    +---------+--------------------------------------------------+
    | Value   |                      Meaning                     |
    +=========+==================================================+
    |   'r'   |  Open existing database for reading only         |
    +---------+--------------------------------------------------+
    |   'w'   |  Open existing database for reading and writing  |
    +---------+--------------------------------------------------+
    |   'c'   |  Open database for reading and writing, creating |
    |         |  it if it doesn’t exist (this is a default value)|
    +---------+--------------------------------------------------+
    |   'n'   |  Always create a new, empty database,            |
    |         |        open for reading and writing              |
    +---------+--------------------------------------------------+
"""

# import the appropriate module and create an object representing a file-based database
import shelve


cost_living_by_country = 'cost_living_by_country.shlv'

cost_shelve = shelve.open(cost_living_by_country, flag='c')
cost_shelve['Kyiv'] = 1700
cost_shelve['Warsaw'] = 2500
cost_shelve['Sofia'] = 2400
cost_shelve['London'] = 4400
cost_shelve.close()

new_cost_shelve = shelve.open(cost_living_by_country)
print(new_cost_shelve['London'])
new_cost_shelve.close()
