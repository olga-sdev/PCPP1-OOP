"""
Metaprogramming is a technique in which computer programs have the ability to modify their own or other programs’ codes.

n many cases metaprogramming allows programmers to minimize the number of lines of code to express a solution,
in turn reducing development time.

But the truth is that this technique could be used for tool preparation; those tools could be applied to your code
to make it follow specific programming patterns, or to help you create a coherent API.

Another example of metaprogramming is the metaclass concept,
which is one of the most advanced concepts presented in this course.

metaclasses redirect class instantiations to dedicated logic, contained in metaclasses.
Metaclasses are applied when class definitions are read to create classes, well before classes are instantiated.

The typical use cases for metaclasses:

* logging;
* registering classes at creation time;
* interface checking;
* automatically adding new methods;
* automatically adding new variables.

Special attributes:
__name__  – inherent for classes; contains the name of the class;
__class__ – inherent for both cls and instances; contains info about the class to which a cls instance belongs;
__bases__ – inherent for classes; it’s a tuple and contains information about the base classes of a class;
__dict__  – inherent for both classes and instances; contains a dictionary of the object's attributes.

"""

elements = [123, False, 'ABC']

for element in elements:
    print(element, 'is: ', element.__class__, '; type: ', type(element))

# 123 is:  <class 'int'> ; type:  <class 'int'>
# False is:  <class 'bool'> ; type:  <class 'bool'>
# ABC is:  <class 'str'> ; type:  <class 'str'>


# type() function is called with three arguments 'Laptop', (), {} -> dynamically created a new class
Laptop = type('Laptop', (), {})

# the argument 'Laptop' specifies the class name; this value becomes the __name__ attribute of the class:
print('The class name is:', Laptop.__name__)
print('The class is an instance of:', Laptop.__class__)

# the argument specifies a tuple () of the base classes from which the newly created class is inherited; this argument becomes the __bases__ attribute of the class
print('The class is based on:', Laptop.__bases__)

# the argument specifies a dictionary {} containing method definitions and variables for the class body; the elements of this argument become the __dict__ attribute of the class and state the class namespace
print('The class attributes are:', Laptop.__dict__)
