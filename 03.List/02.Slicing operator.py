# slice (start: stop: step)
# start is included but stop is excluded

g1 = [1, 233, 445, 32, 24, 32]
p = g1[2: 5: 1]
print(p)

# negative index
new = g1[-1::-1]
print(new)

name = "nikhil"
new = name[-1::-1]
print(new)

#  list tuple
t2 = (3,5,6,2)
t1 = list(t2)
print(type(t1))