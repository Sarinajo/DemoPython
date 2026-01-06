def posneg(numbers):
    pos_sum =0
    negatives =[]

    for num in numbers:
        if num >=0:
            pos_sum +=num
        else:
            negatives.append(num)
    return{
        "positives_sum" : pos_sum,
        "negative": negatives
    }

def oddeven(numbers):
    odd =[]
    even =[]

    for num in numbers:
        if num %2 ==0:
            even.append(num)
        else:
            odd.append(num)
    return{
        "odd":odd,
        "even":even
    }

numbers = [4,-2,6,-8,2,4,1]
posnegresult = posneg(numbers)
oddevenresult = oddeven(numbers)

print(f"the sum of positivies is : {posnegresult['positives_sum']}")
print(f"the negatives in list are : {posnegresult['negative']}")
print(f"the odd numbers in list are {oddevenresult['odd']}")
print(f"the even numbers in list are {oddevenresult['even']}")