class Person:
    def __init__(self, name, occ):#CONSTRUCTOR, invoked whenever an object is made
        print("i am a person")
        self.name = name
        self.occ = occ
    def info(self):
        print(f"Hello {self.name}, you are {self.occ}")
    def hello(self):
        print(f"hello {self.name}")
a= Person("Sarina", "Developer")
b = Person("Alisa", "Nurse")
a.info()
a.hello()
b.info()