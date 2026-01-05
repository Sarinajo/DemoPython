numbers = [4, -2,6,-8,2,4,1]
pos =0
neg =[]
for num in numbers:
    if num >=0:
        pos +=num
    else:
        neg.append(num)
print(pos)
print(neg)
