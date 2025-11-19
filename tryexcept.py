try:
    number1 = int(input("enter the first number: "))
    number2 = int(input("enter the second number: "))

    print(number1/number2)

except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("invalid input ")