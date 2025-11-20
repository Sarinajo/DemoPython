file=open("employee.txt","r")
for msg in file.readlines():
    print(msg)
file.close()