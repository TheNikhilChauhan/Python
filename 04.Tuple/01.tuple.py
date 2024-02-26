# also used to store multiple items in a variable
#  they are ordered, immutable,
# duplicates are allowed, any datatype can be inside it, mix of different data types

# iterating through a tuple is faster than in a list
# Lists are mutable whereas tuples are immutable
# Tuples that contain immutable elements can be used as a key for a dictionary.

t1 = ("blue", "red", 34, 344)



# creating a tuple with 1 item
# fruit = ("apple",)

fruit = tuple("apple")
# check type of tuple
print(type(fruit))
print(len(t1))

#accessing items in tuple
print(t1[1])
print(t1[-1])
print(t1[1:3]) #range indexing
print(t1[-1::-1])

#  traverse in tuple
for i in t1:
    print(i, end=" ")

#concatenate 2 tuples
newT1 = ("green", "yellow")
t1 = t1 + newT1;
print(t1)