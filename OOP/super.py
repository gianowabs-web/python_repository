class Animal:
    def __init__(self, name):
        self.name=name
class dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed=breed

#callbacks
dog1 =dog("Buddy", "Golden retriver")
print(dog1.name)
print(dog1.breed)
print(dog1.name, dog1.breed)
