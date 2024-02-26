
""" x = 0
if x > 0:
    print(x, "is positive")
elif x < 0:
    print(x, "is negative")
# elif x == 0:
else:    
    print(x, "is neither positive nor negative") """
    
# WAP to check which of the two number is greater
p = int(input("Enter first number: "))
q = int(input("Enter second number: "))
if p > q:
    print(p, "is Greater")
# else:
#     print(q, "is Greater")
elif p < q:
    print(q, "is Greater")
else:
    print("Both are equal")