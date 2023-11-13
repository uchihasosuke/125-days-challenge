def isPaldrome(string):
    if string==string[::-1]:
        return "The string is a Palindrome."
    else:
        return "The string is not a Palindrome."
string=input("Enter String:")
print(isPaldrome(string))       