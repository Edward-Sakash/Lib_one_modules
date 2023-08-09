# Python Tools and Libraries

## Modules, imports and pip

In this exercise, we will focus on using imports on modules and on using package manager (pip).
 
## 

## Tasks

### 

### :heavy_plus_sign: Task 1 - modules and imports 

Your task is to create two Python modules called `math_mod.py` and `string_mod.py` and another Python file `script.py`.  
First module should contain functions to:  
  * add,
  * subtract,
  * multiply,
  * and divide two numbers.  

Second module should contain functions to:  
  * concatenate two strings,
  * to create string from list,
  * and to check if string contains at least one digit.  

Next to the both modules third file should contain imports from both modules in the form: `import module` and `from module import something`.   
In your modules you can use modules from Python Standard Library.  
In the third file use all written functions from both modules.
>Hint: You can use [type hints](https://docs.python.org/3/library/typing.html) to gain more experience.
- Your results could look like this:


```bash
Result of adding 4 and 17 is 21
Result of subtracting  33 and 19  14
Result of multiplying  3 and 23 is 69
Result of dividing  44 by 3 is 14.666666666666666
Result of concatenation of 'Hello'' and 'DCI'' is HelloDCI
Result of creating string from list ['Hello'', 'DCI''] is HelloDCI
There is a digit in your string!
Result of checking digits in the string 'HelloDCI007' is True
``` 
 
### :heavy_plus_sign: Task 2 - using pip in virtual environment 

Your task is to practice working with virtual environments and pip:  
  * create [virtual environment](https://docs.python.org/3/tutorial/venv.html) called `env1`,  
  * activate this environment and update pip (read about `--upgrade` flag in documentation of pip or in manual),  
  * install three packages from PyPI (for example `numpy`, `matplotlib`, etc.),
  * create `requirements.txt` file using `freeze` command,
  * create `list.txt` file using `list` command,
  * create `my_script.py` file and use documentation of at least two installed packages (look at the examples) to write working Python program,
  * run the program,  
  * deactivate `env1` and check if program still works,
  * create second virtual environment called `env2` and activate it,  
  * using `install` command of pip (with proper flag) install packages from requirements file,
  * chech if `my_script.py` works in newly created environment.
> Do all sub-tasks given above in one folder!



- Your partial console commands could look like this:


```bash
python3 -m venv ...
source ...
pip install -U ...
pip install ...
pip freeze > ...
python ...

etc.
``` 

# Bonus: Understanding Namespace and Nonlocal Scope in Python
# Part 1: Namespace Exploration
1. Create a Python script named `namespace_demo.py`.
2. Define a global variable `global_var` and assign it a value of your choice.
3. Create a function named `outer_function` that contains a variable `outer_var`.
4. Inside `outer_function`, define a nested function named `inner_function` that contains a variable `inner_var`.
5. Print out the values of `global_var`, `outer_var`, and `inner_var` within their respective scopes.

# Part 2: Nonlocal Scope
1. Add a new function named `nonlocal_demo` within `namespace_demo.py`.
2. Inside `nonlocal_demo`, define a variable `outer_count` and set it to 10.
3. Create a nested function named `inner_increment`, and inside it, define a variable `inner_count` and set it to 5.
4. Increment both `outer_count` and `inner_count` by 1.
5. Print the values of `outer_count` and `inner_count` before and after the increment to observe the changes.