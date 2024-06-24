''' Datatypes in Python '''

''' Primarily these are the following data types in Python: '''
# 1. Integers
# 2. Floating point numbers
# 3. Strings
# 4. Booleans
# 5. None

''' Python automatically identify types of data. '''
a= 71 # identifies a as class <int>
b=88.44 # identifies b as class <float>
name= "harry" # identifies name as class <str>

''' Rules for choosing an identifer '''
# 1) A variable name can contain alphabets, digits, and underscore.
# 2) A variable can only start eith an alphabet and underscore.
# 3) A variable name can't start with a digit.
# 4) No while space is allowed to be used inside a variable name.

''' Operations in python '''
# 1) Arithmetic operators: +,-,*,/ etc.
# 2) Assignment operators: =,+=,-=, etc.
# 3) Comparison operators: ==,>,>=,<,!= etc.
# 4) Logical operators: and,or,not.

''' Type() function and typecasting '''
# type() function is used to find the data type of a given variable in python.
a = 31
print(type(a)) #output: class <int>
b = "31"
print(type(b)) #output: class <str>

# typecasting is used to convert one data type into another.
# There are many function to convert one data type into another,
# Like int(), float(), str(), etc.
c = 31
print(type(str(c))) # integer to string conversion
d = "32"
print(type(int(d))) # string to integer conversion
e = 33
print(type(float(e))) # integer to float conversion

''' input() function '''
# This function allows the user to take input from the keybord as a string.
f = input("Enter you'r name...")
# It is important to note that the output of input is a string(even is a number is entered).
