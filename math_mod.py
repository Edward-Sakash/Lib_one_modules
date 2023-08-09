"""Task 1 - modules and imports
Your task is to create two Python modules called math_mod.py
and string_mod.py and another Python file script.py.
First module should contain functions to:

add,
subtract,
multiply,
and divide two numbers.
Second module should contain functions to:

concatenate two strings,
to create string from list,
and to check if string contains at least one digit.
Next to the both modules third file should contain imports from both
modules in the form: import module and from module import something.
In your modules you can use modules from Python Standard Library.
In the third file use all written functions from both modules.

Hint: You can use type hints to gain more experience.

Your results could look like this:
Result of adding 4 and 17 is 21
Result of subtracting  33 and 19  14
Result of multiplying  3 and 23 is 69
Result of dividing  44 by 3 is 14.666666666666666
Result of concatenation of 'Hello'' and 'DCI'' is HelloDCI
Result of creating string from list ['Hello'', 'DCI''] is HelloDCI
There is a digit in your string!
Result of checking digits in the string 'HelloDCI007' is True
"""

# Solution

# math_mod.py

def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: float, b: float) -> float:
    return a / b
