class bag:
    def __init__(self,data):
        self.data = []
    def add(self,x):
        self.data.append(x)
    def addtwice(self,x):
        self.add(x)
        self.add(x)