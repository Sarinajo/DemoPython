def bonusstatus(name,age,project):
    if age >=18:
        bonus = len(project)*100
        status = "eligible"

    else:
        bonus = 0
        status = "not eligible"
    return bonus, status

name = input("enter you name: ")
age = int(input("enter your age: "))
project = input("enter your projects (seperate with comma)")

projectlist = [p.strip() for p in project.split(",")]

b, s = bonusstatus(name,age,projectlist)
print(f"{name} has {b} bonus and status is {s}")
for pro in projectlist:
    print (pro)