class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def description(self):
        print(f"The car is of {self.brand} brand of {self.model} model made in {self.year} year ")

brand = input("enter the brand: ")
model = input("enter the model: ")
year = input("enter the year: ")

obj = Car(brand,model,year)
obj.description()