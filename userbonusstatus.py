def bonus(name,age,project):
    print(f"{name}'s projects are:")
    for p in project:
        print(p)
    if age >=18:
        bonus = len(project)*100
        status = "eligible"

    else:   
        bonus=0
        status= "not eligible"
    return bonus, status

name = input("enter your name: ")
age = int(input("enter your age: "))

project =[]
while True:
    projects = input("Enter your project: ")
    project.append(projects)
    option = input("More(y/n)")
    if option.lower()=="n":
        break

b , s = bonus(name,age,project)
print(f"{name} has {len(project)} projects and has {b} bonus and is {s} ")
