is_female= False
is_tall=False
if is_female and is_tall:
    print("you are female")
elif is_female and not(is_tall):
    print("not tall")
elif not(is_female) and is_tall:
    print("tall")
else:
    print("You are male")

