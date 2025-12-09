num = [2,8,5,3,6]
print(sorted(num, reverse = True))

users = [{"name": "Sarina" , "bonus" : 200},
         {"name": "Alisa", "bonus" : 300}
         ]
sorted_users = sorted(users, key= lambda x:x["bonus"], reverse= True)

for u in sorted_users:
    print(u["name"],u["bonus"])