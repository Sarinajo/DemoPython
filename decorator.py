def decorator(fx):
    def wrap():
        print("before")
        fx()
        print("after")
    return wrap
@decorator
def hello():
    print("hello")

hello()

def deco(fx):
    def ne():
        print("before")
        fx()
        print("after")
    return ne
@deco
def hello():
    print("hello")
hello()