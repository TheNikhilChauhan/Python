# WAP to find the sum of all items in the dictionary

""" input = {
    "a": 100,
    "b": 200,
    "c": 300
}
sumOF = 0
print(input.values())
for value in input.values():
    sumOF += value;

print(sumOF) """

# given a string and a number N, we need to mirror the characters from N-th position up to the length of the string in alphabetical order. In mirror operation, we change 'a' to 'z', 'b' to 'y' and so on.


input_string = input("Enter string: ")
n = int(input("Enter n: "))

# creating dictionary for mirror operation
alphabets = "abcdefghijklmnopqrstuvwxyz"
reverseAlp = alphabets[::-1]
# print(reverse)


# zip(): to create a dictionary using two different list/string
dict1 = dict(zip(alphabets,reverseAlp))
# print(dict1)

# finding the part of string in which we will do mirror operation
prefix = input_string[0:n-1]
suffix = input_string[n-1:]

# finding the mirror string
mirror = ""
for i in range(0, len(suffix)):
    mirror = mirror + dict1[suffix[i]]

# creating the final string
res = prefix + mirror
print(res)