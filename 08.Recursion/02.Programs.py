# WAP to print numbers from n to 1

# def printNums(x):
#     if x == 0:
#         return 
#     else:
#         print(x)
#         printNums(x-1)
    
# printNums(5)

# print from 1 to n

def printNums(x):
    if x == 0:
        return
    printNums(x-1)
    print(x)

printNums(5)

# print sum from 1 to n
# def printSum(x):
#     # base case
#     if x == 1:
#         return 1
    
#     # recursive case
#     res = x + printSum(x - 1)
#     return res

# n = int(input("Enter the number: "))
# print(printSum(5))

# ***************************

# make a function which calculates 'a' raised to the power 'b' using recursion

def exp(a,b):

    # base case
    if b == 0:
        return 1 

    # recursive case
    res = a * exp(a, b-1)
    return res

print(exp(2, 4));

# *******************************

# make a function which calculates fibonacci sequence using recursion.
def fib(x):

    #base
    if x == 1:
        return 0
    elif x == 2:
        return 1
    else:
        return (fib(x - 1) + fib(x-2))
    
x = int(input("Enter num: "))
for i in range(1, x+1):
    print(fib(i))