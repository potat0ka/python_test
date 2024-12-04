#arithemetic operator +, -, *, /,%
#logical operator and, or, not
#assigement operator =
#comparision operator <, >, <=, >=, ==, !=
#bitwise operator = || 
# // 

#print (6//9)
#print(4%2) 

"""WAP to perform addition, sub ,mult of two any number"""
a = 6
b = 9
print(7 // 2)  # Output: 3 (integer part of 7 ÷ 2)
print(7.5 // 2)  # Output: 3.0 (still floored but as a float)
print (f"Addition of {a} and {b} is" , a+b)
print (f"Subtraction of {a} and {b} is" , a-b)
print (f"Multiplication of {a} and {b} is" , a*b)

""" 
Use of `end` in `print()`  
The `end` parameter decides what to add **at the end** of the printed line instead of a new line (`\n`).  

Example:  
print("Hello World", end=", ")  
print("How are you?")  

Output:
Hello World, How are you?  


Logical Operators  
Logical operators help check multiple conditions and say **yes (True)** or **no (False)**.  
1. and 
   - Says "yes" only if **both conditions are true**.  
   - Example:   
     print(5 > 3 and 4 > 2)  # Yes, both are true  
2. or
   - Says "yes" if **at least one condition is true**.  
   - Example:   
     print(5 > 3 or 4 < 2)  # Yes, one is true  
3. not 
   - Flips the answer: "yes" becomes "no," and "no" becomes "yes."  
   - Example:  
     print(not(5 > 3))  # No, it flips "yes" to "no"  
""" 

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