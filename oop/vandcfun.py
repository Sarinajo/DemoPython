def clean_string(text):
    return ''.join(char.lower() for char in text if not char.isspace())

def analyze_string(text):
    vowel = consonant = digits = specials =0

    for c in text:
        if c.isalpha():
            if c in "aeiou":
                vowel +=1
            else:
                consonant +=1
        elif c.isdigit():
            digits +=1
        else:
            specials +=1
    return vowel,consonant,digits,specials

text = "Sarina 1 Joshi"
cleaned = clean_string(text)
v,c,d,s = analyze_string(cleaned)

print(v,c,d,s)

