numbers = [1,5,3,2,5,3,7]
if numbers:
    largest = numbers[0]
    for num in numbers[1:]:
         if num >largest:
             largest = num
print(largest)