# Write a program to fill in a letter template given below with name and date.
""" 
letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
''' 
"""

Name = input("Enter your name...")
Date = input("Enter the date...")
letter = f'''
Dear {Name},
You are selected!
{Date}
'''
print(letter)

