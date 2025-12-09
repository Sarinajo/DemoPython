def greet(name="Sarina",country="Nepal"):
    print(f"{name} lives in {country}")

greet("Alisa", "USA")

def add(a,b):
    return a+b

result = add(10,20)
print(result)

def num(numbers):
    return max(numbers),min(numbers)

big , small = num([1,2,3,4]) #the list is being pased as one boject
print(big,small)