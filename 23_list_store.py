#WAP to take user inout 5 friend data and store it in total_list
#total_data=[[ram,]]
#print()

total_list=[]
print(total_list)

total_list = [['rahul',9889,'ktm'],]
for i in range(1,6):
    name=input("enter user name ")
    mobile_number = input("enter mobile number ")
    location = input("Enter Location ")

    user_data = []
    user_data.append(name)
    user_data.append(mobile_number)
    user_data.append(location)

    total_list.append(user_data)