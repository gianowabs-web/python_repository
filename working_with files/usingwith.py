#python automatically closes the file for you
with open("names.txt", "a") as file: # "a" = append
 file.write("\nAdding another line safely.")

with open("names.txt", "r") as file:
 print(file.read())