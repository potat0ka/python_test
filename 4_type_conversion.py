name = "aris"
age_1 = "30"  # Age as a string
age = 31  # Age as an integer
salary = 2.5  # Salary as a float

# Check the type of variables
print(type(age))  # Outputs: <class 'int'>
print(type(age_1))  # Outputs: <class 'str'>

# Convert salary from float to integer
int_salary = int(salary)  # Float-to-integer conversion
print(type(int_salary))  # Outputs: <class 'int'>
print(int_salary)  # Outputs: 2 (the decimal is removed)



# ### Explanation of Fixes:

# 1. Variable `age`:
#    - You used `age = "31"` initially, which would make `age` a string.
#    - Changed `age` to `31` (an integer) so that `type(age)` correctly outputs `<class 'int'>`.

# 2. Float to Integer Conversion (`int(salary)`):
#    - The `int()` function converts a float to an integer by truncating the decimal part.
#    - Example: `2.5` becomes `2`.

# 3. Syntax Consistency:
#    - Ensured all variable names and usage are correct and consistent with Python conventions.



# Outputs:
# `type(age)`: `<class 'int'>` because `age` is now an integer.  
# `type(age_1)`: `<class 'str'>` because `age_1` is a string (`"30"`).  
# `type(int_salary)`: `<class 'int'>` because `salary` was converted to an integer using `int()`.  
# `int_salary` Value: `2`, as `2.5` is truncated.  


# Important Notes:
# 1. Conversion Removes Decimals:
#    - When converting `float` to `int`, only the whole number part is retained. No rounding is performed.  
#    - Example: `3.9` becomes `3`.

# 2. Why Type Conversion?
#    - Type conversion is often required when operations involve incompatible types (e.g., adding an integer and a string).  

# 3. sage of `type()`:
#    - The `type()` function is used to check the data type of a variable in Python.