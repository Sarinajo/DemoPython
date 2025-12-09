def num(*numbers):
    return max(numbers),min(numbers)

big,small = num(1,2,3,4,5,6)

print(big,small)

def print_names(*names):
    for name in names:
        print(name)

print_names("Sarina","Alisa","kritigya")

#kwargs

def details(**detail):
    print(detail)
    for key, value in detail.items():
        print(f"{key}:{value}")
    print(detail["name"])

details(name="Sarina", age=23, city="Kathmandu")