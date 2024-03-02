# strings are a sequence of characters within '', "", "''"
# Strings are immutable but we can create a new string by manipulating original string.

str1 = 'This is a single quote string'
str2 = "This is a double quote string"
str3 = '''This is a triple quote string'''

print(str1, str2, str3)

# multiline string to a variable

para = '''
    This is a 
    multiline string.
'''

print(para)

# array-like indexing in strings

text = "Hello World"

print(text[4])
print(text[8])
print(text[-1]) #last index 'd' 
print(text[-1::-1])


# traversing a string

for i in text:
    print(i, end=',')

# using list comprehension
list = [char for char in text]
print(list)
for i in list:
    print(i)

# find() index in string
# find(): returns the index of first occurenc of the character/substring.
# /it returns -1 if not found in string
print(text.find('o'))

