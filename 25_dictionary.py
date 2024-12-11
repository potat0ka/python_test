# print(type({}))

user_data = {}
user_data_detail = {"name":"skill shikshya","number":"+97798080"}

#priint (user_data_detail["names"])

#user_data_detail["name"] = "ram"
#print(user_data_detail)
'''
for key in user_data_detail:
    pass
{"name":"skill shikshy","number":"+97798080"}
'''
# user_data = {}
# user_data_detail = {"name":"skill shikshy","number":"+97798080"}
# print("User Name:", user_data_detail["name"])
# user_data_detail["name"]="Ram"
# print("Updated details: ", user_data_detail)
# for key in user_data_detail:
#     print(f"{key}:{user_data_detail[key]}")

for key in user_data_detail:
    if key == "number":
        user_data_detail["number"]="977" + user_data_detail["number"]

print(user_data_detail)        


#make a software which store students and their subjects marks.