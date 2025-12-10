class dog:
    species = "Canine"
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.tricks=[]
        

    def description(self):
        return f"{self.name} is {self.age} years old"
    def bark(self,sound):
        return f"{self.name} says {sound}"
    def birthday(self):
        self.age +=1
        return f"{self.name}is {self.age} now"
    def add_tricks(self,trick):
        self.tricks.append(trick)
    def show_tricks(self):
        if self.tricks:
            for t in self.tricks:
                print(f"{self.name} can do {t}")
        else:
            print("no tricks yet")
    def play_with(self,other_dog):
        return f"{self.name} is playing with {other_dog.name}"


    

dog1 = dog("puntu",1)
print(dog1.name)
print(dog1.description())
print(dog1.bark("woof"))
print(dog1.birthday())
print(dog1.birthday())
print(dog1.species)
dog1.add_tricks("roll over")
dog1.add_tricks("play")
dog1.show_tricks()

dog2 = dog("jhayammu",5)
print(dog2.description())
print(dog2.bark("woof"))
dog2.add_tricks("play")
dog2.show_tricks()

print(dog1.play_with(dog2))
