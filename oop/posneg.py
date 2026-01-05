def analyze_numbers(numbers):
    pos = 0
    neg =[]
    for num in numbers:
        if num >=0:
            pos +=num
        else:
            neg.append(num)
    return pos , neg

positivesum , negatives = analyze_numbers([4,-2,5,1,6,3,-5,-3])
print(positivesum)
print(negatives)
