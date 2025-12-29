word= "sarina joshi ! hello"
start = 0

is_palindrome= True
cleanword = ''.join(char.lower() for char in word if char.isalpha())
end = len(cleanword)-1
while start<end:
    if cleanword[start]!= cleanword[end]:
        is_palindrome = False
        break
    start +=1
    end -=1
print(is_palindrome)