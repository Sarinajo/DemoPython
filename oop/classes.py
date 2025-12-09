class dog:
    def __init__(self,name,age,sound):
        self.name = name
        self.age = age
        self.sound = sound

    def description(self):
        return f"{self.name} is {self.age} years old"
    def bark(self):
        return f"{self.name} says {self.sound}"
    



dog1 = dog("puntu",1,"woof")
print(dog1.name)
print(dog1.description())
print(dog1.bark())