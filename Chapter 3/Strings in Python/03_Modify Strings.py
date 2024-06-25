''' Modify Strings in Python '''
# Python strings are immutable, meaning they cannot be changed once created.
# However, you can create a new string that is a modified version of the original string.

# Here are some ways to modify strings in Python:

''' (1) Upper Case '''
# The "upper()" method converts all lowercase characters in a string to uppercase.
# Example:-
str1 = "hello world!"
print(str1.upper())  # Output: HELLO WORLD!

''' (2) Lower Case '''
# The "lower()" method converts all uppercase characters in a string to lowercase.
# Example:-
str2 = "HELLO WORLD!"
print(str2.lower())  # Output: hello world!

''' (3) Remove Whitespace '''
# The "strip()" method removes any leading or trailing whitespace from a string and ending.
# Example:-
str3 = " Hello, World! "
print(str3.strip()) # Output: Hello, world!

''' (4) Replace String '''
# The "replace()" method replaces a specified phrase with another specified phrase.
# Example:-
str4 = "Hello, World!"
print(str4.replace("H", "K")) # Output: Kello, World!

''' (5) Split String '''
# The "split()" method splits a string into a list where each word is a list item.
# Example:-
str5 = "Hello, World!"
print(str5.split(",")) # Output: ['Hello', 'World!']

''' Important Note '''
# There are many String Methods on internate go and learn them, we only cover those we used most.