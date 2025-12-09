skills=["javascript","python","java"]
skills.append("SQL")
for skill in skills:
    print(skill)

Tuple = ("Python","Javascript")
print(Tuple[0])
#we can't change the tuple. we can't perform add, edit delete type of operations but we can convery the tuple into list and perform those operations and then change the list back to tuple. what we can also do is we can concatenate two tuples
List = list(Tuple)
List.append("SQL")
print(List)
Tuple2 = tuple(List)
print(Tuple2)

user={"name": "Sarina", "age": 23, "skil":["Python","Django"]}
print(user['name'],user["age"], user['skil'])
