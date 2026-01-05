word = "Sarina 1 Joshi"
if word:
    cleanword = "".join(char.lower() for char in word if char.isalpha())
    countv = 0
    countc = 0
    for c in cleanword:
        if c in "aeiou":
            countv +=1
        else:
            countc +=1
print(countv)
print(countc)    