# script.py

# script.py

from math_mod import add, subtract, multiply, divide
from string_mod import concatenate_strings, create_string_from_list, contains_digit

# Math operations
a = 4
b = 17
print(f"Result of adding {a} and {b} is {add(a, b)}")
print(f"Result of subtracting {a} and {b} is {subtract(a, b)}")
print(f"Result of multiplying {a} and {b} is {multiply(a, b)}")
print(f"Result of dividing {a} by {b} is {divide(a, b)}")

# String operations
s1 = "Hello"
s2 = "DCI"
print(f"Result of concatenation of '{s1}' and '{s2}' is {concatenate_strings(s1, s2)}")

lst = ['Hello', 'DCI']
print(f"Result of creating string from list {lst} is {create_string_from_list(lst)}")

s = "HelloDCI007"
print(f"Result of checking digits in the string '{s}' is {contains_digit(s)}")
