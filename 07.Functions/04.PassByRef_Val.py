#  pass by reference  and pass by value

# Pass by value
""" 
They are immutable objects, strings, integers, float, typles
When passed to a function, a copy of the object is created and assigned to a local variable in a function.
If any change is made to them inside function, do not affect the original object outside the function.

"""

def addOne(x):
    x = x + 1
    print("Inside function:",x)

x = 5
addOne(x)
print("Outside function:",x)

# Pass by reference
""" 
They are mutable objects like list, dictionary
A reference to actual object is passed to function
Changes inside the function will affect the original object.
 """

def modifyList(l):
    l.append(5)
    print("Inside function:",l)

l = [1,2,3]
modifyList(l)
print("Outside function:", l)