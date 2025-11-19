# def is used to write function
def say_hi(name, age):
   print("hi " + name + " you are " + age )

print("Top")
say_hi("sarina", "23")
print("Bottom")
name = input("enter the name: ")
say_hi(name, "23")


def cube(num):
   three = num * num * num
   print("cube of " + str(num) + "is" + str(three))


cube(3)