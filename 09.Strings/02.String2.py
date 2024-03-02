'''
methods : upper(), lower(), capitalize()
        stripe(), replace(), slice(),
        concatenation, format()
'''

# slicing a string

text = "My name is Nikhil Chauhan"
print(text[3: 11]) #starting and ending(is not included)

print(text[-3:])

# modifying strings
# upper(): converting characters to upper case
str1 = "Delhi"
str2 = str1.upper() #it returns a new string
print(str2)
print(str1)

# lower()
print(str1.lower())

# capitalize(): the first letter of the string
print(str2.capitalize())

# stripe(): for stripping/removing any trailing whitespace
str3 = "   hi there!"
print(str3.strip())


# replace()
# string.replace(old_substring, new_substring, count)
str4 = "hi there, nikhil. What can I help you with nikhil?"
# str5 = str4.replace("nikhil", "Mr. Chauhan")
str5 = str4.replace("nikhil", "Mr. Chauhan", 1)
print(str5)

# count in the replace() is used for the occurence. If we don't use it then it will replace the word with all the occurence of the old_substring


# split(): used to split the string into a list of substrings
# string.split(sep, maxsplit) , seperator, maxsplit: how many times we want to split at the separation.

string1 = "hey there, could you be any older?"
list = string1.split(",",2)
print(list)

# concatenation
string2 = "hello world!"
string3 = "what a great place this is."
print(string2 + string3)

# format(): used to insert value in a string

student_name = "Harvey"
student_marks = 77

string11 = "The student name is {s} and merks is {m}".format(s= student_name, m = student_marks)
print(string11)