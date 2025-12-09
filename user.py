users = [{"name": "Sarina","age":23,"projects":['Python','Javascript']},
         {"name":"Alisa","age":23,"projects":['Python','java']},
         {"name": "Kritigya","age":24,"projects":['Python','C#']}]
         

for user in users:
    if user["age"] == 23:
        bonus = len(user["projects"])*10
        print(user["name"] + f" has {bonus} bonus")
        user["bonus"]=bonus

for user in users:
    print(user)
    
my_set = set({1,2,3,4,4,4})
print(my_set)
my_set.add(5)
print(my_set)

