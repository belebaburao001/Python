''' Fotmat String in Python '''
# As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:

# Example:-
# age = 36
# str1 = "My name is John, I am " + age
# print(str1) # Output: Error


''' F-Strings '''
# But we can combine strings and numbers by using f-strings or the format() method!

# F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.

# To specify a string as an f-string, simply put an "f" in front of the string literal, and add curly brackets "{}" as placeholders for variables and other operations.

# Example:-
age = 26
str2 = f"My name is Jhon, I am {age}"
print(str2) # Output: My name is Johan, I am 26


''' Placeholders and Modifiers '''
# A placeholder can contain variables, operations, functions, and modifiers to format the value.

# Example 01:- Add a placeholder for the "price" variable:
price = 49
str3 = f"The price is {price} dollars"
print(str3) # Output: The price is 49 dollars

# Example 02:- Display the price with 2 decimals:
# A placeholder can include a modifier to format the value.
# A modifier is included by adding a colon : followed by a legal formatting type, like "".2f" which means fixed point number with 2 decimals:
price = 59
str4 = f"The price is {price:.2f} dollars"
print(str4) # Output: The price is 59.00 dollars

# Example 03:- A placeholder can contain Python code, like math operations:
str5 = f"The sum of 1 + 1 is: {1 + 1}"
print(str5)