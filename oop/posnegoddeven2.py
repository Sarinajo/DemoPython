def analyze_posneg(numbers):
    possum =0
    neg = []

    for num in numbers:
        if num >=0:
            possum +=num
        else:
            neg.append(num)

    return possum,neg

def analyze_oddeven(numbers):
    odd =[]
    even =[]

    for num in numbers:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    
    return odd,even

def analyze_numbers(numbers):
    pos_sum , negatives =analyze_posneg(numbers)
    odd , even =analyze_oddeven(numbers)

    return{
        "positive_sum": pos_sum,
        "negatives": negatives,
        "odd" : odd,
        "even": even
    }
    
numbers = [1,2,4,6,-2,7,9,-8,-5]
result = analyze_numbers(numbers)
'''print(result["positive_sum"])
print(result["negatives"])
print(result["odd"])
print(result["even"])'''
for key,value in result.items():
    print(f"{key}:{value}")