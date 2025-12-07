words = ["Python", "js" , "SQL"]
print(words)
print(words[0])
print(words[-1])
print(words[-2])

for word in words:
    print(f"i know {word}")

i=0
while i < len(words):
    print("i know" + words[i])
    i +=1


age = [18,19,20,21,22,23]

for a in age:
    if a< 18:
        print(f"{a} is underage")
    else:
        print(f"{a} isn't underage")

projects = ["SQL","Python","js"]

for project in projects:
    print(f"Project is {project}")

i=0
while i < len(projects):
    print(f"project is {projects[i]}")
    i +=1

users = [{"name": "Sarina", "age": 23},
         {"name": "Alisa", "age": 23},
         {"name": "Kritigya", "age":24 },
         {"name": "Shristi", "age":17}
         ]

for user in users:
    if user["age"] <=18:
        print(f"{user["name"]} is underage")
    else:
        print(f"{user["name"]} isn't underage")

i=0
while i < len(users):
    user = users[i]
    if user["age"] <18:
        print(f"{user["name"]} is underage")
    else:
        print(f"{user["name"]} isn't underage")
    i +=1