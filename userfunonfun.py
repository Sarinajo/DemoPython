def calculate_bonus(project):
    return len(project)*100

def get_status(age):
    if age >= 18:
        status = "eligible"
    else:
        status = "not eligible"
    return status

def user_print():
    name = input("enter your name: ")
    age = int(input("enter your age: "))

    projects = []
    while True:
        project = input("enter your project: ")
        projects.append(project)
        option = input("more(y/n): ")
        if option.lower() == "n":
            break
    return {"name": name,"age":age,"projects":projects}

def print_summary(user):
    bonus = calculate_bonus(user["projects"])
    stat = get_status(user["age"])

    print(f"{user['name']} has {bonus} bonus and is {stat}")


users = []

while True:
    user = user_print()
    users.append(user)

    more = input("Add another user (y/n): ")
    if more.lower()=="n":
        break 


for user in users:
    print_summary(user)

