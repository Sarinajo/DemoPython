friends = ["Alisa","Renusha", "Puja", "sneha" , "Hissie"]
print(friends)
print(friends[0])
print(friends[-1])
print(friends[1:]) # index 1 paxi ko grab garxa
print(friends[1:3]) # index first dekhi 3 bich ko grab grxa
friends[4]="sarina"
print(friends)

#list functions
lucky_numbers = [4,7,9,8]
friends = ["Alisa","Renusha", "Puja", "sneha" , "Hissie"]
friends.append("Sarina")
friends.insert(1,"Aayusha")
print(friends)
friends.extend(lucky_numbers) # friends and lucky are together
print(friends)
friends.remove("Aayusha")
print(friends)
print(friends.pop())
print(friends)
print(friends.index("Sarina"))
lucky_numbers.sort()
print(lucky_numbers)
print(friends)
lucky_numbers2 = lucky_numbers.copy()
print(lucky_numbers2)