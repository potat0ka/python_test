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