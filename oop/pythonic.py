numbers = [1,-2,3,-4,5]
pos_sum = sum(num for num in numbers if num >=0)
print(pos_sum)
neg = [num for num in numbers if num<0]
print(neg)
odd = [num for num in numbers if num % 2 !=0]
print(odd)
even =[num for num in numbers if num % 2 ==0]
print(even)
