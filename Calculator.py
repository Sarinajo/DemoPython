num1 = float(input("enter the first num: "))
num2 = float(input("enter the second num: "))

operation = input("what operation? \n"
                  "1. Add\n"
                  "2. Sub\n"
                  "3. Div\n"
                  "4. Mul\n")

if operation == "1":
     print(num1 + num2)
elif operation == "2":
    print(num1 - num2)
elif operation == "3":
    print(num1 / num2)
elif operation == "4":
    print(num1 * num2)
else:
    print("invalid")