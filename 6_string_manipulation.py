first_name = "aris"
second_name = "sarad"

print (first_name+second_name) #concat

a = "aris"
b = 9
print (a+str(b))

first_sentence = " hello I am from mars  "

print(first_sentence.strip())

skill_shikshya = "skillshikshya@gmail.com"
splitted_data = skill_shikshya.split('@')
print(splitted_data)


about_nepal = "nepal is .....nepal .. kahsiudqe alasdkdlkqpqoei india ... iasjd .. india"
corrected_data = about_nepal.replace('india','nepal')
corrected_data = corrected_data.replace('.','the')
print(corrected_data)

father_name = "some name"
print(father_name.upper())
print(father_name.capitalize())
print(father_name.title())

#describe any 10 string manipulating function in python
text = "hello world"
print(text.capitalize())
# Convert the first character to uppercase # Output: Hello world

print(text.casefold())
# Convert the string to lowercase (more aggressive than lower) # Output: hello world

text = "Hello"
print(text.center(10, "-"))
# Center the string with a specified width and padding character # Output: --Hello---

text = "apple apple banana"
print(text.count("apple"))
# Count occurrences of a substring # Output: 2

text = "Hello"
print(text.encode())
# Encode the string using UTF-8 # Output: b'Hello'

text = "Hello, world!"
print(text.endswith("!"))
# Check if the string ends with the specified value # Output: True

text = "H\te\tl\tl\to"
print(text.expandtabs(4))
# Set the tab size of the string # Output: H   e   l   l   o

text = "Hello, world!"
print(text.find("world"))
# Find the first occurrence of a substring # Output: 7

text = "Hello, {}!"
print(text.format("world"))
# Format specified values into the string # Output: Hello, world!

data = {"name": "Alice", "age": 25}
text = "My name is {name} and I am {age} years old."
print(text.format_map(data))
# Format values using a dictionary or mapping object # Output: My name is Alice and I am 25 years old.

text = "Hello, world!"
print(text.index("world"))
# Find the index of a substring (raises error if not found) # Output: 7

text = "Hello123"
print(text.isalnum())
# Check if all characters are alphanumeric # Output: True

text = "Hello"
print(text.isalpha())
# Check if all characters are alphabetic # Output: True

text = "Hello"
print(text.isascii())
# Check if all characters are ASCII # Output: True

text = "12345"
print(text.isdecimal())
# Check if all characters are decimals # Output: True

text = "12345"
print(text.isdigit())
# Check if all characters are digits # Output: True

text = "variable_name"
print(text.isidentifier())
# Check if the string is a valid Python identifier # Output: True

text = "hello"
print(text.islower())
# Check if all characters are lowercase # Output: True

text = "12345"
print(text.isnumeric())
# Check if all characters are numeric # Output: True

text = "Hello"
print(text.isprintable())
# Check if all characters are printable # Output: True

text = "   "
print(text.isspace())
# Check if all characters are whitespace # Output: True

text = "Hello World"
print(text.istitle())
# Check if the string follows title case # Output: True

text = "HELLO"
print(text.isupper())
# Check if all characters are uppercase # Output: True

fruits = ['Apple', 'Orange', 'Banana']
print(", ".join(fruits))
# Join elements of an iterable into a string # Output: Apple, Orange, Banana

text = "Hello"
print(text.ljust(10, "-"))
# Return a left-justified version of the string # Output: Hello-----

text = "HELLO"
print(text.lower())
# Convert all characters to lowercase # Output: hello

text = "   Hello"
print(text.lstrip())
# Remove leading whitespace # Output: Hello

trans_table = str.maketrans("aeiou", "12345")
text = "hello"
print(text.translate(trans_table))
# Replace characters based on a translation table # Output: h2ll4

text = "Hello, world!"
print(text.partition(", "))
# Split the string into three parts: before, separator, after # Output: ('Hello', ', ', 'world!')

text = "Hello, world!"
print(text.replace("world", "Python"))
# Replace a substring with another # Output: Hello, Python!

print(text.rfind("o"))
# Find the last occurrence of a substring # Output: 8

print(text.rindex("o"))
# Find the last occurrence of a substring (raises error if not found) # Output: 8

print(text.rjust(10, "-"))
# Return a right-justified version of the string # Output: -----Hello

print(text.rpartition("l"))
# Split the string into three parts, starting from the right # Output: ('Hel', 'l', 'o')

csv_text = "Apple,Orange,Banana"
print(csv_text.rsplit(",", 1))
# Split a string into a list, starting from the right # Output: ['Apple,Orange', 'Banana']

text = "Hello   "
print(text.rstrip())
# Remove trailing whitespace # Output: Hello

csv_text = "Apple,Orange,Banana"
print(csv_text.split(","))
# Split a string into a list # Output: ['Apple', 'Orange', 'Banana']

text = "Hello\nWorld"
print(text.splitlines())
# Split a string at line breaks # Output: ['Hello', 'World']

print(text.startswith("He"))
# Check if the string starts with the specified value # Output: True

text = "   Hello   "
print(text.strip())
# Remove leading and trailing whitespace # Output: Hello

text = "Hello, World"
print(text.swapcase())
# Swap the case of all characters # Output: hELLO, wORLD

text = "hello world"
print(text.title())
# Convert the first character of each word to uppercase # Output: Hello World

print(text.translate(trans_table))
# Translate the string using a translation table # Output: h2ll4

text = "hello"
print(text.upper())
# Convert all characters to uppercase # Output: HELLO

text = "42"
print(text.zfill(5))
# Pad the string with zeros on the left # Output: 00042

"""
What is `!=` Operator?  
The `!=` operator checks if **two values are not equal**.  
- It says **True** if the values are **different**.  
- It says **False** if the values are **the same**.  

#### Example:  
print(5 != 3)  # True, because 5 is not equal to 3  
print(5 != 5)  # False, because 5 is equal to 5   

---

### Bitwise Operators  
Bitwise operators work with the **binary form** of numbers (0s and 1s).  

Types of Bitwise Operators:  
1. **`&` (AND)**  
   - If both bits are `1`, the result is `1`. Otherwise, it’s `0`.  
   - Example:   
     print(5 & 3)  # Output: 1  
     # 5 in binary:  101  
     # 3 in binary:  011  
     # AND:          001 (1 in decimal)  


2. **`|` (OR)**  
   - If at least one bit is `1`, the result is `1`.  
   - Example:  
     print(5 | 3)  # Output: 7  
     # 5 in binary:  101  
     # 3 in binary:  011  
     # OR:           111 (7 in decimal)   

3. **`^` (XOR)**  
   - The result is `1` if the bits are different, `0` if they are the same.  
   - Example:  
     print(5 ^ 3)  # Output: 6  
     # 5 in binary:  101  
     # 3 in binary:  011  
     # XOR:          110 (6 in decimal)  

4. `~` (NOT)
   - Flips all bits (changes `0` to `1` and `1` to `0`).  
   - Example:   
     print(~5)  # Output: -6  
     # 5 in binary:  00000101  
     # NOT:          11111010 (which is -6 in decimal due to two's complement representation)  

5. `<<` (Left Shift)
   - Moves bits to the left, adding `0`s at the end. Each shift multiplies the number by 2.  
   - Example:  
     print(5 << 1)  # Output: 10  
     # 5 in binary:   101  
     # Left shift:   1010 (10 in decimal)  
 

6. `>>` (Right Shift)
   - Moves bits to the right, removing bits from the end. Each shift divides the number by 2.  
   - Example:  
     print(5 >> 1)  # Output: 2  
     # 5 in binary:   101  
     # Right shift:    10 (2 in decimal) 
"""