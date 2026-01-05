word = "hell 3onepalhe llobetterlife"
if word:
    countv = 0
    countc = 0
    newword = ''.join(char.lower() for char in word if char.isalpha())
    for v in newword:
            if v in "aeiou":
                countv +=1
            else:
                countc +=1
print(f"count of vowel:{countv}")
print(f"count of consonant{countc}")

