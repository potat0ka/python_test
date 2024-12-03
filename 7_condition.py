"""
Types of condition
1)if  
2)if ...else
3)if ...elif ...else(nested conditions)
"""
age=13
if age>18: #false
    print("you can vote")

age=20
if age>18: #true
    print("you can Drink")

# syntax
# if condition_true:
#     statements    

# syntax
# if condition_false:
#     no_statements

age=13
if age>18: #false
    print("you can vote")
else:
    print("you can't vote")    

# Wap to output like {child,adult...old}
age = "A"
if isinstance(age,str) and not age.isdigit(): #if isinstance(age,str) and age.isdigit() == False:
    print("invalid age")
elif age > 0 and age < 13:
    print("you are child")
elif age >=13 and age <= 20:
    print("you are teenager")
elif age >20 and age <= 60:
    print("you are adult")
elif age <= 0 or age > 100: #true or false = true
    print("wrong input")    
else:
    print("you are old")     