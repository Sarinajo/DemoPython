def calculate_bonus(name,age,project):
    if age >=18:
        bonus = len(project)*10
        return(f"{name} has {bonus} bonus points")
    else:
        return(f"{name} is underage so no bonus")

#calculate_bonus("sarina",23,4)

users = [{"name":"Sarina","age":23,"project": ['Python','Django']},
         {"name": "Alisa","age":23,"project": ['Java','SQL']},
         {"name": "Shristi","age":17,"project":['Java','SQL','Django']}
         ]

for user in users:
    
    message = calculate_bonus(user["name"],user["age"],user["project"])
    print(message)