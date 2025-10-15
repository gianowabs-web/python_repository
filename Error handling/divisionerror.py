# when something goes wrong (like dividing by zero or trying to read a missing file)
# python throws an error instead of crashing , we can handle errors using try and except.

# handling division error

try:
    x = int(input("Enter a number:"))
    y = int(input("Enter another number:"))
    result= x/y
    print("Result", result)
except ZeroDivisionError:
    print("! you can't divide by zero!")# when you divide a number by 0 
except ValueError:
    print("Please enter valid numbers!")# incase you type a letter then its displayed
 
 #Handling missing files
try:
    with open("divisionerror.py", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("! File was not found")

# the finally block always runs, useful for cleanup
try:
    with open("names.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("! File was not found")
finally:
    print("This runs no matter what")
    