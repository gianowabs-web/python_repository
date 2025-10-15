def greet(name="Gian", age = 23):
    print("hello,", name,"is your age", age)
greet() # uses the default 
greet("David", 25) # overrides default

#create a function called square that takes a number as input and returns 
#its square.

def square(square= 4**2 ,square2= 9**2):
    print("square", square ,"square", square2)
square()

# alterative
def square(num):
    return num * num
print(square(4))
print(square(9))
     
