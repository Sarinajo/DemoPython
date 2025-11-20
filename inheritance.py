class person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def info(self):
        print(f"hello {self.fname} {self.lname}")
class student(person):
    pass #if i don't wnat any method and function of the class function itself but want to use parent's
class teacher(person):
    def __init__(self,fname,lname):
        person.__init__(self,fname,lname)
x=person("sarina","joshi")
y=student("alisa","lamsal")
z=teacher("puja","bhatta")
x.info()
y.info()
z.info()
