""" name = "Harvey"
for letter in name:
    print(letter) """

name = "Harvey"
for letter in name:
    print(letter, end="")
print('\n')


# range(stop)
for i in range(5):
    print(i,"Hello")
print(end='\n')
# range(start, stop)
for i in range(5, 7):
    print(i,"Hello")

print(end='\n')

# range(start, stop, step)
for i in range(5, 15, 3):
    print(i,"Hello")