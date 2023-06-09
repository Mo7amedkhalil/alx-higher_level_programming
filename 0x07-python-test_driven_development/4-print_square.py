#!/usr/bin/python3
"""

module that includes 'print_square' function

"""


def print_square(size):
    """ Function that prints a square of 'size' length of #
    Args:
        size : integer

    Returns:
        Success

    Raises:
        TypeError:
                size is not integer
        ValueError:
            size < 0
    """
    size_err = 'size must be an integer'
    zero_err = 'size must be >= 0'

    if type(size) is not int:
        raise TypeError(size_err)
    if size < 0:
        raise ValueError(zero_err)

    ay_my_name.py'

-------------------------

Using 'say_my_name'

-------------------------

Importing function from module
>>> say_my_name = __import__('3-say_my_name').say_my_name

passing empty strings
>>> say_my_name("", "")
My name is  

passing 2 correct strings
>>> say_my_name("first", "last")
My name is first last

passing strings of 1 character
>>> say_my_name("f", "l")
My name is f l

passing strings of numbers
>>> say_my_name("3", "4")
My name is 3 4

passing the first string only
>>> say_my_name("mo")
My name is mo 

passing strings of None as values
>>> say_my_name("None", "None")
My name is None None

passing strings of underscores
>>> say_my_name("_", "_")
My name is _ _

passing empty first_name
>>> say_my_name("", "last")
My name is  last

passing empty last_name
>>> say_my_name("first", "")
My name is first 

passing second argument as None
>>> say_my_name("first", None)
Traceback (most recent call last):
	...
TypeError: last_name must be a string

passing first_name as None
>>> say_my_name(None, "last")
Traceback (most recent call last):
	...
TypeError: first_name must be a string

passing integer
>>> say_my_name(4, "last")
Traceback (most recent call last):
	...
TypeError: first_name must be a string

passing last_string as integer
>>> say_my_name("first", 5)
Traceback (most recent call last):
	...
TypeError: last_name must be a string

passing 2 integers
>>> say_my_name(5, 5)
Traceback (most recent call last):
	...
TypeError: first_name must be a string

passing 2 None arguments
>>> say_my_name(None, None)
Traceback (most recent call last):
	...
TypeError: first_name must be a string

passing Boolean values
>>> say_my_name(False, True)
Traceback (most recent call last):
	...
TypeError: first_name must be a string

passing nan strings
>>> say_my_name('nan', 'nan')
My name is nan nan

passing only last_name argument
>>> say_my_name(last_name = 'nan')
Traceback (most recent call last):
	...
TypeError: say_my_name() missing 1 required positional argument: 'first_name'

passing string and float
>>> say_my_name('nan', 3.5)
Traceback (most recent call last):
	...
TypeError: last_name must be a string

passing 3 arguments
>>> say_my_name('nan', 3.5, 'nano')
Traceback (most recent call last):
	...
TypeError: say_my_name() takes from 1 to 2 positional arguments but 3 were given

passing first_name as float
>>> say_my_name(3.5, 'nano')
Traceback (most recent call last):
	...
TypeError: first_name must be a string

passing no args
>>> say_my_name()
Traceback (most recent call last):
	...
TypeError: say_my_name() missing 1 required positional argument: 'first_name'

passing 1 for first_name
>>> say_my_name(1)
Traceback (most recent call last):
	...
TypeError: first_name must be a stringor i in range(size):
        print('#'*size)
