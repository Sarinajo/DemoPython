word = "Sarina 1 Joshi"
if word:
    countv = 0
    countc= 0
    countd = 0
    counts = 0
    for c in word:
        if c.isalpha():
            if c.lower() in "aeiou":
                countv +=1
            else:
                countc +=1
        elif c.isdigit():
            countd +=1
        elif c.isspace():
            pass
        else:
            counts +=1
print(countv)
print(countc)
print(countd)
print(counts)
                
