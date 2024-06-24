import os

# Define the path of the directory
directory_path = '/'

# Get the list of all files and directories in the specified directory
contents = os.listdir(directory_path)

# Print the contents
for item in contents:
    print(item)