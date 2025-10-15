maths = int(input("Enter your maths marks:"))
english= int(input("Enter your eng marks:")) 
kiswahili=int(input("Enter your kis marks:"))
science =int(input("Enter Your sci Marks:"))
social_studies =int(input("Enter your sst marks:"))  
average= (maths+ english+kiswahili+science+social_studies)

if average >= 390:
    print("Grade: A")
elif average >= 350:
    print("Grade: B")
elif average >= 320:
    print("Grade: B-")
elif average >= 280:
    print("Grade: C+")
elif average >= 250:
    print("Grade: C")
elif average >= 200:
    print("Grade: C-")
else:
    print("Grade: Fail")
    

