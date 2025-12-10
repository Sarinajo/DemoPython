class Dog:
    species = "canine"
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def bark(self):
        return f"{self.name} barks"
    
    @classmethod
    def change_species(cls,new_species):
        cls.species = new_species

    @staticmethod
    def is_puppy(age):
        return age<2
    
d = Dog("puntu",1)
print(d.bark())
Dog.change_species("Wolf")
print(Dog.is_puppy(1))
print(d.species)

        