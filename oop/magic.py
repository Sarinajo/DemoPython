class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
d= Dog('Puntu',3)
print(d)
        