"""
About extended function arguments (args):

functions without args;
functions with specific number of args with no exclusions;
functions with defined default values for params -> keyword params;
pass args in any order in case of assigning keywords to all arg values, otherwise positional -> first on the args list.

Special identifiers (*args and **kwargs) -> last two params in a function definition. Their names could be changed.

*args – refers to a tuple of all additional, not explicitly expected positional args;
**kwargs (keyword args) – refers to a dict {} of all unexpected args that were passed in form of keyword=value pairs.


"""

# Case 1
def print_params(param, *args, **kwargs):
    super_print_params(*args, **kwargs)


def super_print_params(*super_args, **super_kwargs):
    print(super_args, type(super_args))
    print(super_kwargs, type(super_kwargs))


print_params('parameter', 'another parameter', 1, 2, 3, arg1='arg1', arg2=2)
# ('another parameter', 1, 2, 3) <class 'tuple'>
# {'arg1': 'arg1', 'arg2': 2} <class 'dict'>


# Case 2
def print_params(param, *args, **kwargs):
    super_print_params(args, kwargs)


def super_print_params(*super_args, **super_kwargs):
    print(super_args, type(super_args))
    print(super_kwargs, type(super_kwargs))


print_params('parameter', 'another parameter', 1, 2, 3, arg1='arg1', arg2=2)
# (('another parameter', 1, 2, 3), {'arg1': 'arg1', 'arg2': 2}) <class 'tuple'>
# {} <class 'dict'>


# Case 3
def print_params(param, *args, other_param=True, **kwargs):
    super_print_params(other_param, *args, **kwargs)


def super_print_params(super_param, *super_args, **super_kwargs):
    print(super_param, type(super_param))
    print(super_args, type(super_args))
    print(super_kwargs, type(super_kwargs))


print_params('parameter', 'another parameter', 1, 2, 3, other_param=False, arg1='arg1', arg2=2)
# False <class 'bool'>
# ('another parameter', 1, 2, 3) <class 'tuple'>
# {'arg1': 'arg1', 'arg2': 2} <class 'dict'>
