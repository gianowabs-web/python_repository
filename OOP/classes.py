# OOP is a way of organizing codes into classes (blueprint) and
#objects (real things created from the blue print).
# it helps code made reusable and structured

class person:
    def __init__(self,name, age):
        self.name=name
        self.age=age

    def greet(self):
        print(f"Hello, my name is {self.name} and i am {self.age} years old.")
    def is_adult(self):
        return self.age >= 18
    
    
# creating object
p1 =person("Alice", 17)
print(p1.is_adult())
p2 =person("Gian", 23)
print(p2.is_adult())

p1.greet()
p2.greet()
p1.is_adult()

# updating attributes
p1.age= 28
p1.greet()
p2.name= "Given"
p2.greet()


# adding another method

      