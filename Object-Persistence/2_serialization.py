"""
Serialization -> process of converting an object structure into a stream of bytes to store the object in a file or DB,
or to transmit it via a network.
This byte stream contains all the information necessary to reconstruct the object in another Python script.

This reverse process is called deserialization.

Python objects can also be serialized using a module called 'pickle'.

The following types can be pickled:

None, booleans;
integers, floating-point numbers, complex numbers;
strings, bytes, bytearrays;
tuples, lists, sets, and dictionaries containing pickleable objects;
objects, including objects with references to other objects (remember to avoid cycles!)
references to functions and classes, but not their definitions.


Serialization is an essential process in many applications and systems because it enables the following:

1. Data Persistence
Serialization allows data to be saved and later restored, ensuring that the state of an application can be retained between sessions.
For example, user preferences in an application can be stored in a file and loaded when the application is restarted.

2. Data Transmission
Serialized data can be easily transmitted over a network between different components of a distributed system.
This is fundamental in web services, APIs, and MS where data needs to be shared across different systems or platforms.

3. Interoperability
Serialization allows data to be converted into a standard format that can be understood by different programming languages.
For instance, JSON serialization enables Python apps to communicate with JavaScript-based web applications.

4. Efficient Storage and Retrieval
Serialized data can be stored in a compact format, making it efficient for storage and retrieval from databases or files.
This is particularly useful when dealing with large volumes of data.

5. Remote Procedure Calls (RPC)
Serialization is critical in RPC systems where methods are invoked over a network.
Data structures and parameters are serialized, sent to the remote system, and then deserialized to execute the procedure.

6. Logging and Debugging
Serialized data can be used for logging and debugging purposes, capturing the state of an object at a specific point in time.
This makes it easier to analyze and reproduce issues.

7. Caching
Serialization allows data to be cached in an efficient manner, speeding up the retrieval process and reducing the load on the original data source.
This is commonly used in web applications to cache responses from databases or external APIs.

Exceptions:
* attempts to pickle non-pickleable objects will raise the PicklingError exception;
* trying to pickle a highly recursive data structure may exceed the max recursion depth, and a RecursionError is raised;
*

the function name is pickled


the pickle module is not secured against erroneous or maliciously constructed data. 
Never unpickle data received from an untrusted or unauthenticated source.
"""

# Example with Serialization with pickle python module
import pickle

cost_of_living = {
    'Kyiv': 1700,
    'Warsaw': 2500,
    'Sofia': 2400,
    'London': 4400,
}

# the file handle 'file_out' is associated with the file opened for writing in binary mode
with open('data.pckl', 'wb') as file_out:
    # persist the object with the dump() function
    pickle.dump(cost_of_living, file_out)

# Example with Deserialization

# the file is opened in binary mode and the file handle is associated with the file
with open('data.pckl', 'rb') as file_in:
    # read some portions of data and deserialize it with the load() function
    data = pickle.load(file_in)

print(type(data))
print(data)

# serialized objects could be persisted in a database or sent via a network
schengen_countries = [
    "Austria", "Belgium", "Czechia", "Denmark", "Estonia", "Finland",
    "France", "Germany", "Greece", "Hungary", "Iceland", "Italy",
    "Latvia", "Liechtenstein", "Lithuania", "Luxembourg", "Malta",
    "Netherlands", "Norway", "Poland", "Portugal", "Romania",
    "Slovakia", "Slovenia", "Spain", "Sweden", "Switzerland"
]

"""pickle.dumps(object_to_be_pickled) – expects an initial object, returns a byte object. 
This byte object should be passed to a database or network driver to persist the data;"""
bytes = pickle.dumps(schengen_countries)
print('Intermediate object type, used to preserve data:', type(bytes))

"""therefore when you receive a bytes object from an appropriate driver you can deserialize it
pickle.loads(bytes_object) – expects the bytes object, returns the initial object"""
schengen_area = pickle.loads(bytes)
print('A type of deserialized object:', type(schengen_area))
print('Contents:', schengen_area)


# Example with Class
class Laptop:
    def __init__(self):
        self.weight = 2

    def get_weight(self):
        return self.weight


laptop = Laptop()

with open('laptop.pckl', 'wb') as file_out:
    pickle.dump(laptop, file_out)

with open('laptop.pckl', 'rb') as file_in:
    data = pickle.load(file_in)

print([type(data), data, data, data.get_weight()])

# [<class '__main__.Laptop'>, <__main__.Laptop object at 0x0000014BD1216930>,
# <__main__.Laptop object at 0x0000014BD1216930>, 2]
