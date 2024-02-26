# store in key-value pairs

""" 
1. They are in ordered form.
2. They are changable
3. They are unindexed.We can't access them using index
4. Duplicate values are not allowed.
5. Any datatype can be stored in dictionary.
 """

# phone = {
#     "Chandler": 45242625,
#     "Joey": 89285-23,
#     "Ross": 3458203958,
# }

# printing the dict
""" print(phone)

print(type(phone))
# access
print(phone["Ross"])
print(phone.get("Joey"))
print(phone.keys())

# update value in dict
phone["Chandler"] = 89843943453
print(phone)

# add elements in dict
# phone["Rachel"] = 98898942490
# print(phone)
# if I use the same name with different phone number then number will only get updated 

more_phone = {
    "Rachel": 98898942490
}
phone.update(more_phone)
print(phone)

# remove the element from dict
phone.pop("Rachel")
print(phone)

phone.popitem() #this will remove the last addeed item
print(phone)

# phone.clear()
# print(phone)

# iterate through dict by printing elements
for x,y in phone.items():
    print(x, y) """
    
# nested dictionary
phone = {
    "Area1": {
        "x": 0,
        "y": 1,
        "z": 2,
    },
    "Area2": {
        "a": 3,
        "b": 4,
        "c": 5
    }
}

print(phone["Area1"]["y"])
print(phone["Area2"]["c"])