# text = "The unexpected always happens." 

# # print(text)
# print(len(text))
# print(text.find('pp'))
# print(text[:11])
# # print(text.replace("always", "never"))
# text.replace("always", "never")
# new_str = "no matter what"
# print(text + new_str)


# write a function that checks if the given string is a palindrome or not
def checkPalindrome(text):
    # clean string
    clean_str = (text.replace(" ","")).lower()
    p = clean_str[::-1]
    if (clean_str == p):
        print(text, "is a palindrome")
    else:
        print(text, "is not a palindrome")

n = str(input("Enter a string: "))
checkPalindrome(n)