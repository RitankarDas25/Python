#Dictionaries store data in key : value pair
# its unordered , mutable , dont allow dublicate keys
# key cannot be a list or dictionary
info = {
    "key" : "value",
    "name" : "Ritankar",
    "age": 22,
    "marks" : [45.7,56.8,89.7],
    12.89 : True
}
print(info)

# access values
print(info["name"])
print(info["marks"])

# change value
info["name"]="Ritz"
info["surname"]="Das" # add new key value
print(info)

#nested dictionaries

student = {
    "name" : "Ritankar",
    "subjects" : { #another dictionary
        "maths" : 98,
        "english": 89,
        "phy": 78
    }
}

print(student)
print(student["subjects"]) # prints inner dictionary
print(student["subjects"]["phy"]) # prints the value of phy

# methods
print(list(student.keys())) # prints all keys of outter dict
print(len(student)) # no .of key value pairs
print(student.values()) # prints all values
print(student.items()) # returns all key value pairs as tuples
print(student.get("name")) # returns value of the key else returns none if key not present
student.update({"city" : "ccu"})# adds new key values or updates existing key with new value
print(student)