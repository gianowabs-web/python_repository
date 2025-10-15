#reading line by line
file = open("example.txt", "r")
for line in file:
    print(line.strip()) # strip removes extra spaces/ newline
file.close()
