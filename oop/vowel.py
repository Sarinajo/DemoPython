word = "sarina"
if word:
    count = 0
    for char in word:
        if char.lower() in "aeiou":
            count +=1
    print(count)
else:
    print("empty string")