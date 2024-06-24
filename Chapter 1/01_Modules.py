''' Modules in python '''
# A module is a file containing code written by somebody else (usually) which can be imported and used in our program.

''' Types of Modules '''
# 1. Built-in Modules: These are modules that come pre-installed with Python.
# Some examples of Built-in Modules are; math, os, random etc
import math

# Calculate the square root of 16
print(math.sqrt(16))  # Output: 4.0

# 2. External Modules: These are modules that need to install usign pip.
# Some examples of Extrnal Modules; pyttsx3, tensorflow, flask etc
import pyttsx3
engine = pyttsx3.init()
engine.say('''
This is an example of External module in python,
where it able to convert text to voice!
''')
engine.runAndWait()
 