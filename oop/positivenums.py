numbers = [4,-2,6,-8,2,4,1]
if numbers:
    total = 0
    negatives = []
    for num in numbers:
        if num >0:
            total +=num
        else:
            negatives.append(num)
    print(total)
    if negatives:
        print(negatives)
