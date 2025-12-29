word = "Sarina"
reverse = ""
if word:
    for char in range(len(word)-1,-1,-1):
        reverse +=word[char]

print(reverse)