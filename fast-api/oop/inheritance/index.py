class Parent():
    def __init__(self, name, age):
        self.name = name
        self.age  = age
    
    def __str__(self):
        return f"name: {self.name}, age: {self.age}"
    
class Childrent(Parent):
    pass

class Childrent2(Parent):
    def __init__(self, name, age, year):
        super().__init__(name, age)
        self.year = year
    
    def __str__(self):
        return f"name: {self.name}, age: {self.age} - year: {self.year}"
        
        
c1 = Childrent("Dat", 23)
print(c1.__str__())

c2 = Childrent2("Tu", 22, 2002)
print(c2.__str__())

