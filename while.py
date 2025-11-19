i=1
while i<=10:
    print(i)
    i +=1

    if i% 5 ==0:
        what = input("Stop or continue: ")
        if what.lower() == "stop":
            break

print("done")

i=30
while i>=20:
    print(i)
    i -=1
print("done")
