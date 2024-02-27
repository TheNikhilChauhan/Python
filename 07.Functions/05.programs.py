# WAP to calculate the factorial of a number(non-negative). The function accepts the number as an argument.

def factorialOfNum(x):
    fact = 1
    if x == 0:
        return 1
    else:
        for i in range(1, x+1):
            fact *= i

    return fact

output = factorialOfNum(5)
print(output)