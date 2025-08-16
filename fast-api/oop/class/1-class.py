# create a class
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name  = last_name
        
    def __str__(self): 
        return f"{self.first_name}_({self.last_name})"
    
    def reverse_name(self):
        return f"{self.last_name}_{self.first_name}"

p1 = Person('dat', 'truong')
# print(p1)
# print(str(p1))
print(p1.reverse_name())