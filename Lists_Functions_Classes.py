class Vehicle:
    def __init__(self, Vehicle_Type):
        self.Vehicle_Type = Vehicle_Type

class Automobile(Vehicle):
    def __init__(self, Vehicle_Type, year, make, model, doors, roof):
        super().__init__(Vehicle_Type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

def user_car():
    Vehicle_Type = "Car"
    year = input("Year of car: ")
    make = input("Maker of car: ")
    model = input("Model of car: ")
    doors = input("2 or 4 doors: ")
    roof = input("Sun roof, convertible, or hard top: ")

    Car = Automobile(Vehicle_Type, year, make, model, doors, roof)
    return Car

def display_user_car(Car):
    print("Type of vehicle:", Car.Vehicle_Type)
    print("Year of car:", Car.year)
    print("Make of car:", Car.make)
    print("Model of car:", Car.model)
    print("Number of doors:", Car.doors)
    print("Roof type:", Car.roof)


Car = user_car()
print()
display_user_car(Car)