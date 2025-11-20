class Person:
    name = "Sarina"
    occupation ="Student"
    networth = 100000
    def info(self):
        print(f"Hello {self.name}, you are {self.occupation}")

a= Person()
b= Person()
c = Person()

a.name ="Alisa"
a.occupation="Nurse"
b.name = "Puja"
a.info()
b.info()
c.info()
