# Recursion is a technique where a function calls itself in order to solve a problem. The problem is broken down into smaller instance of the problem
# factorial using recursion
def factorialOfNum(n):
    
    if n ==0:
        return 1;
    
    # recursive case
    ans = n * factorialOfNum(n-1)
    return ans

n = int(input("Enter a number: "))
print(factorialOfNum(n))