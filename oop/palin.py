word = "A man, a plan, a canal: Panama"
if word:
    cleanword = " ".join(char.lower() for char in word if char.isalpha())
    start = 0
    end = len(cleanword)-1
    is_palindrome = True
    while start< end:
        if cleanword[start] != cleanword[end]:
            is_palindrome = False
        start +=1
        end -=1
print(is_palindrome)

