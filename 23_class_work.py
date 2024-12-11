# a=5
# b=9
# print("before swap value of a is : ",a)
# print("before swap value of b is : ",b)
# ....
# ....

a = 5
b = 9

print("Before swap:")
print("Value of a is:", a)
print("Value of b is:", b)

c=a #5
a=b #9
b=c #5

# a, b = b, a .i.e without using swap/temp variable

print("\nAfter swap:")
print("Value of a is:", a)
print("Value of b is:", b)

data = [2,5,6,7,3 ] #output must be [4,25,36,49,9]
output = []

for i in data:
    output.append(i**2)
print(output)