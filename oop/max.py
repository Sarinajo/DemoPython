def analyze_numbers(numbers):
    pos_sum =0
    negatives =[]
    max_num = None

    for num in numbers:
        if num >=0:
            pos_sum +=num
        else:
            negatives.append(num)
        
        if max_num is None or num >max_num:
            max_num = num
    
    return{
        "positives_sum" : pos_sum,
        "negatives" : negatives,
        "max_number": max_num

    }

numbers=[2,-3,-8,1,6,7,8,2]
result = analyze_numbers(numbers)
print(result["positives_sum"])
print(result["negatives"])
print(result["max_number"])