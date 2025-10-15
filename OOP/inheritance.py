# basic inheritance
class Animal:
    def __init__(self, name):
        self.name=name
    def speak(self):
        print(self.name + "makes a sound")
    
#child class
class dog(Animal):
    def speak(self):
        print(self.name + "barks")
class cat(Animal):
    def speak(self):
        print(self.name + "meows")
# callbacks
dog1= dog("Buddy ")
cat1= cat("Whiskers ")

dog1.speak()
cat1.speak()


    