class Base:
    def greet(self):
        return "Hello from parent"
    
class Child(Base):
    def greet(self):
        return Base.greet(self)
    def greet_Child(self):
        return "Hello from child"

d = Child()
print(d.greet())
print(d.greet_Child())
print(isinstance(d,Child))
print(issubclass(Child,Base))