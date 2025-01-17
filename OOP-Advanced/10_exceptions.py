"""
Exception handling
When code may raise an exception, use TRY: problematic_code EXCEPT code block to surround "problematic" piece of code.
In effect, when the exception is raised, execution is not terminated.

Advanced exceptions - named attributes:
Example_1: ImportError exception – raised when the import statement has trouble trying to load a module.
The attributes are:
* name – represents the name of the module that was attempted to be imported;
* path – represents the path to any file which triggered the exception, respectively. Could be None.

Example_2: UnicodeError exception – raised when Unicode-related encoding/decoding error occurs. Subclass of ValueError.
The UnicodeError has attributes that describe an encoding or decoding error.
* encoding – the name of the encoding that raised the error.
* reason – a string describing the specific codec error.
* object – the object the codec was attempting to encode or decode.
* start – the first index of invalid data in the object.
* end – the index after the last invalid data in the object.


Chained exceptions (Exception chaining):
* additional exception (implicit chaining);
* translate exception to another type (explicit chaining).

Attributes of exception instances:
* the __context__ attribute, which is inherent for implicitly chained exceptions;
* the __cause__ attribute, which is inherent for explicitly chained exceptions.


"""

# Example_1: ImportError
try:
    import abra_cadabra_module

except ImportError as import_err:
    print(import_err.args)
    print(f'Name of module that was attempted to be imported: {import_err.name}')
    print(f'Path to any file which triggered the exception: {import_err.path}')

# ("No module named 'abra_cadabra_module'")
# Name of module that was attempted to be imported: abra_cadabra_module
# Path to any file which triggered the exception: None


# Example_2: UnicodeError
try:
    '你好!'.encode("ascii")
except UnicodeError as uni_err:
    print(f'Error: {uni_err}')
    print(f'Name of the encoding that raised an error: {uni_err.encoding}')
    print(f'String desribing the specific codec error: {uni_err.reason}')
    print(f'Object the codec was attempting to encode or decode: {uni_err.object}')
    print(f'First index of invalid data in the object: {uni_err.start}')
    print(f'Index after the last invalid data in the object: {uni_err.end}')

# Error: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)
# Name of the encoding that raised an error: ascii
# String desribing the specific codec error: ordinal not in range(128)
# Object the codec was attempting to encode or decode: 你好!
# First index of invalid data in the object: 0
# Index after the last invalid data in the object: 2


# Example_3: implicitly chained exceptions
new_json = {}

try:
    new_json.popitem()
except Exception as err:
    try:
        print(new_json['name'])
    except KeyError as key_err:
        print('Inner exception', key_err)
        print('Outer exception', err)
        print('Outer exceptions referenced', key_err.__context__)
        print('Is it the same object:', key_err.__context__ is err)


# Inner exception 'name'
# Outer exception 'popitem(): dictionary is empty'
# Outer exceptions referenced 'popitem(): dictionary is empty'
# Is it the same object: True


# Example_4: explicitly chained exceptions


class ApplicationIsNotFull(Exception):
    pass


def check_application():
    """
    Explicitly chained exceptions is translated exception to another type
    """
    try:
        print('Name', job_application['name'])
        print('Title', job_application['title'])
        print('CV', job_application['cv'])
        print('Work Permission', job_application['work_permission'])
    except KeyError as key_e:
        raise ApplicationIsNotFull('Application is not completed') from key_e


def test_check():
    try:
        print(f'Test is completed in {100/0}%')
    except ZeroDivisionError as zero_err:
        raise ApplicationIsNotFull('Test is not started yet') from zero_err


job_application = {
    'name': 'Olga',
    'title': 'QA Engineer',
    'cv': True,
}

check_list = [check_application, test_check]

for check in check_list:
    try:
        check()
    except ApplicationIsNotFull as app_e:
        print(f'General exception {app_e} caused by {app_e.__cause__}')

# Name Olga
# Title QA Engineer
# CV True
# General exception Application is not completed caused by 'work_permission'
# General exception Test is not started yet caused by division by zero
