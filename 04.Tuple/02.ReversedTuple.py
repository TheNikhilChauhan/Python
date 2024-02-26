# function to reverse tuple
t1 = (2,565,23,13)
for x in reversed(t1):
    print("Reversed:",x)

input_tuple = (1,2,3,4,5,6)
list = []

# adding reversed values in a list
for x in reversed(input_tuple):
    list.append(x)

output_tuple = tuple(list)
print(output_tuple)