# Creating and Removing Directories:
import  os

# Create a new directory
os.mkdir('new_directory')
# Remove an existing directory
os.rmdir('new_directory')


# Renaming and Deleting Files:
# Rename a file
os.rename('old_name.txt', 'new_name.txt')
# Delete a file
os.remove('new_name.txt')


# Checking for File Existence:
# Check if a file exists
file_exists = os.path.exists('my_file.txt')
print(file_exists)
# Check if it is a file or directory
is_file = os.path.isfile('my_file.txt')
is_dir = os.path.isdir('my_directory')
print(is_file)
print(is_dir)


# Using `open` with Context Manager:
# Using open to read a file
with open('my_file.txt', 'r') as file:
    contents = file.read()
    print(contents)

# Using open to write to a file
with open('my_file.txt', 'w') as file:
    file.write('Hello, world!')