def max_num(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        print(f"{num1} is greater")
    elif num2 >= num1 and num2 >= num3:
        print(f"{num2} is greater")
    else:
        print(f"{num3} is graeter")

number1 = input("enter 1st: ")
number2 = input("enter 2nd: ")
number3 = input("enter 3rd: ")

result = max_num(number1,number2,number3)