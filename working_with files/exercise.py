#Write a program that ask the user to enter their name 
 # and then saves it into a file called names.txt
name= input("Enter your name:")
 #open file in append mode so names are added, not overwritten

with open("names.txt", "a") as file:
    file.write(name + "\n")

print("Your name has been saved to names.txt")