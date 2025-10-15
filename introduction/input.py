# Using input() in python
name = input("Enter name:")
age= input("Enter age:")
is_student=input("Are you a student (yes/no):")

print("my name is", name,"and I am", age, "years old also a student", is_student)
# this prompt the user at the console to enter there name, age and status 
# input() always return the text (a string),even if you type a number.
#if you want a number you must convert it

age = int(input("Enter your age:")) # convert it to integer.
height=float(input("Enter your height:")) #convert to decimal.

print("I am", age,"years old and my height is", height, "m2.")
