users = [{"name":"Sarina","skills":['Python','Django']},
         {"name":"Alisa","skills":['Python','Sql']},
         {"name": "Kritigya","skills":['Java','CSS']}
         ]

unique_skills = set()
for user in users:
    for skill in user["skills"]:
        unique_skills.add(skill)
print(f"unique skills are {unique_skills}")

