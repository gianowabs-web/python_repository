# create a program with the following classes 
# 1 vehicle (parent class)
#  attributes: brand : <brand> , Model: <model>
#  car ( child class of vehicle )
#  Extra attributes : doors
#  Overide info() => prints number of doors
# 3. bike (child class of vehicle)
#   Extra attribute : engine_cc
#  Override info() => pints engine capacity

class Vehicle:
    def __init__(self, brand, model):
        self.brand=brand
        self.model=model
class car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors=doors
class bike(car):
    def __init__(self, brand, model, doors, engine_cc):
        super().__init__(brand, model, doors)
        self.engine_cc=engine_cc
veh=Vehicle("Buggati", "sports")
car1 =car("Buggati", "sportscar", "34 by 19")
bike1=bike("Yamaha", "sportsbike","none", "KenineY9")

print(veh.brand, veh.model)
print(car1.brand, car1.model, car1.doors)
print(bike1.brand, bike1.model, bike1.doors, bike1.engine_cc)


        