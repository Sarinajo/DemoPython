def greet(name):
    return f"hello {name}"

def welcome(name):
    message = greet(name)
    print (message + ". Welcome to Python Learning")

welcome("Sarina")


def add(a,b):
    return a+b

def sum(a,b):
    result = add(a,b)
    return result , result *2

total, double = sum(2,3)
print(f"sum is {total} and it's twice is {double}")