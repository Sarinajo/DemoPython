user = input("enter you name :")
age = int(input("enter your age: "))
projects = int(input("enter the numbe yesof projects you have done: "))
print(f"Hello {user} ! You are {age} years old and have completed {projects} projects.")
if age <18:
    print("you are underage,access restricted")
else:
    print("access granted")

bonus = projects *10

print(f"you bonus points: {bonus}")