word = "123a321"
if word:
    start =0
    cleanword = ''.join(char.lower() for char in word if char.isalnum())
    end = len(cleanword)-1
    is_palindrome = True
    while start < end:
        if cleanword[start] != cleanword[end]:
            is_palindrome = False
            break
        start +=1
        end -=1
print(is_palindrome)
