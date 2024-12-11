# name  = "kathmandu"  #

# for letter in name:
#     if "m" in letter:
#         print("m is present congrats")
#     full_letter = "@"+letter
#     print(full_letter)

# num = 5 
# a= 6.5
first_data = ['apple','ball','cat','dog']
# Wap to diplay below format output
#    it is apple
#    it is ball
#    it is cat
#    it is dog
for first_data in first_data:
    print (first_data)
# for i in range(1, 6):
#     if i == 3:
#         continue 
#     print(i)

first_data = ['apple','ball','cat','dog','elephant'] #list
#Wap to display below format output
# it is an apple
# it is  a ball
# it is a cat
# it is a dog
# it is an elephant
for first_data in first_data:
    if first_data[0] in "aeiou":
        print("it is an " + first_data)
    else:
        print("it is a " + first_data)
