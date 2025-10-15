# open file in write mode ("W")
file= open("names.txt", "a")
file.write("Hello this is my first file!\n")
file.write("python makes file handling easy.")
file.close()

#  appending adding text
file=open("names.txt", "a")
file.write("\n Given wabs is sick.")
file.close()
