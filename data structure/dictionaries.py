# store data in key-value pairs

person ={
    "name" : "Gian",
    "age": 25,
    "city": "Nairobi"
}
print(person["name"]) # access Gian
person["age"]= 26    # update value
person["job"]= "Engineer" # add new key
print(person)


# create an object and manipulate the data in the object access, update , add and print final output

dog = {
    "name": "Bosco",
    "breed": "German Shephard",
    "color": "Black n White",
    "tag size": 18
}
print(dog["tag size"])
dog["tag size"]=10
dog["accomplishment"]= "Bronze medal"
dog["color"]="brown"
print(dog)