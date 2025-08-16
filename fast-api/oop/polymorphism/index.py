class Vehicle():
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def move(self):
        print("Move!")
        
class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print("Sail!")
        
class Plane(Vehicle):
    def move(self):
        print("Fly!")
        
car   = Car("Ford", "C1")
boat  = Boat("Ibiza", "B1")
plane = Plane("VNA", "P1")

for x in (car, boat, plane):
    print(x.brand)
    print(x.model)
    x.move()
    print("-----")