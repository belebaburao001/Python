''' Strings in Python '''
# Strings in python are surrounded by single quotation marks, or double quotation marks.
# We can also display a string literal with the "print()" function.
# Example:-
print("Hello, World!")
print('Hello, World!')


''' Quotes Inside Quotes '''
# If we want to display a string that contains quotes, we can use single quotes inside double quotes.
# Example:-
print("It's alright")
print("This is 'Python' notes!")
print('This is "Python" notes!')


''' Assign String to a Variable '''
# Assigning a string to a variable is done with the variable name followed by an equal sign and the string:
# Example:-
str1 = 'Hello, World!'
str2 = "Hello, World!"
print(str1) # Output: Hello, World!
print(str2) # Output: Hello, World!


''' Multiline Strings '''
# We can assign a multiline string to a variable by using three Double or Single quotes:
# Example:-
str3 = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(str3)
str4 = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(str4)


''' String Length '''
# The len() function returns the length of a string.
# Example:-
str5 = "Hello, World!"
print(len(str5)) # Output: 13


''' Check String '''
# We can check if a certain phrase or character is present in a string with the keyword "in".
# Example:-
str5 = "The best things in life are free!"
print("free" in str5) # Output: True


''' Check if NOT '''
# We can check if a certain phrase or character is NOT present in a string with the keyword "not in".
# Example:-
str6 = "The best things in life are free!"
print("expensive" not in str6) # Output: False


''' Indexing in Python '''
# Python uses zero-based indexing, which means the first character in the string is at index 0
# Example:-
str7 = "Hello, World!"
print(str7[0])  # Output: H
print(str7[7])  # Output: W

''' Negative Indexing '''
# Negative indexing starts from the end of the string.
# Example:-
str8 = "Hello, World!"
print(str8[-1])  # Output: ! (last character)
print(str8[-5])  # Output: W (5th character from the end)