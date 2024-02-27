# Types of arguments
# function which takes 2 numbers as input and returns their sum

# def add(n1, n2 = 5):
#     sum = n1 + n2;
#     return sum;

# # positional argument
# print(add(2,3))

# # named argument
# print(add(n1=2, n2=3))

# # default argument
# print(add(3))

# arbitary arguments *args
def addAllNums(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

output = addAllNums(2,3,4,5)
print("The sum is:", output)

# kwargs: keyworded argument/ key-value pairs of arguments
def studentInfo(**kwargs):
    for x,y in kwargs.items():
        print(x,"is", y)

studentInfo(name="Chandler", age=32, city="New York")

