''' Slicing in Python '''
# We can axis a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon, to return a part of the string.
# Example:-
str1 = "Hello, World!"
print(str1[2:5]) # Output: llo


''' Slice From the Start '''
# By leaving out the start index, the range will start from the first character.
# Example:-
str2 = "Hello, World!"
print(str2[:5]) # Output: Hello


''' Slice To the End '''
# By leaving out the end index, the range will go to the end of the string.
# Example:-
str3 = "Hello, World!"
print(str3[7:]) # Output: World!