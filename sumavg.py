def sumavg(numbers):
    total = sum(numbers)
    avg = total/len(numbers)
    return total,avg

t, a = sumavg([1,2,3,4,5])
print(f"sum is {t} and average is {a}")

def bonusstatus(name,age,project):
    if age >=18:
        bonus = len(project)*10
        status = "eligible"

    else:
        bonus = 0
        status = "underage"
    return bonus , status

name = "Sarina"
b , s = bonusstatus(name,23,["Python","Django"])
print(f"{name} has {b} bonus and is {s}")

