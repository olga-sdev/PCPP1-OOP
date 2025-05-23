"""
Objectives
improving the student's skills in operating with different kinds of exceptions.

Scenario
Try to extend the checklist script to handle more different checks, all reported as RocketNotReady exceptions.
Add your own checks for: batteries and circuits.
"""


class RocketNotReadyError(Exception):
    pass


def personnel_check():
    try:
        print("\tThe captain's name is", crew[0])
        print("\tThe pilot's name is", crew[1])
        print("\tThe mechanic's name is", crew[2])
        print("\tThe navigator's name is", crew[3])
    except IndexError as e:
        raise RocketNotReadyError('Crew is incomplete') from e


def fuel_check():
    try:
        print('Fuel tank is full in {}%'.format(100/0))
    except ZeroDivisionError as e:
        raise RocketNotReadyError('Problem with fuel gauge') from e


def batteries_check():
    try:
        print('Battery is full level {}%'.format(100/0))
    except ZeroDivisionError as e:
        raise RocketNotReadyError('Problem with battery') from e


def circuits_check():
    try:
        print('Circuit level', circuit['level'])
    except KeyError as e:
        raise RocketNotReadyError('Problem with circuit level') from e


crew = ['John', 'Mary', 'Mike']
fuel = 100
circuit = {}
check_list = [personnel_check, fuel_check, batteries_check, circuits_check]

print('Final check procedure')

for check in check_list:
    try:
        check()
    except RocketNotReadyError as f:
        print('RocketNotReady exception: "{}", caused by "{}"'.format(f, f.__cause__))


# Final check procedure
# 	The captain's name is John
# 	The pilot's name is Mary
# 	The mechanic's name is Mike
# RocketNotReady exception: "Crew is incomplete", caused by "list index out of range"
# RocketNotReady exception: "Problem with fuel gauge", caused by "division by zero"
# RocketNotReady exception: "Problem with battery", caused by "division by zero"
# RocketNotReady exception: "Problem with circuit level", caused by "'level'"
