#Ask the user to enter their name and age.
# save the information into a file (data.txt);
# Read the file back and show the saved info

name = input("Enter your name")
Age = input("Enter your age")

with open("data.txt", "a") as file:
    file.write("Your name is" + name +"\n")
    file.write("Your age is" + Age + "\n")
with open("data.txt", "r") as file:
    print(file.read())



