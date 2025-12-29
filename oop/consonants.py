word = "sarina"
if word:
    count = 0
    for char in word:
        if "a"<= char.lower() <="z":
            if char.lower() not in "aeiou":
                count +=1
    print (count)
else:
    print("empty string")