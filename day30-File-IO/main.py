# Opening and Reading from a File
# Example 1: Reading the entire contents of a file
with open('file.txt', 'r') as file:
    contents = file.read()
    print(contents)


# Writing to a file
# Example 2: Writing to a file (this will overwrite the file if it exists)
with open('file.txt', 'w') as file:
    file.write('Hello, World!')

# Reading back the contents to verify
with open('file.txt', 'r') as file:
    contents = file.read()
    print(contents)


# Appending to a File
# Example 3: Appending to a file (this will add to the file if it exists)
with open('file.txt', 'a') as file:
    file.write('\nAppended Line.')

# Reading back the contents to verify
with open('file.txt', 'r') as file:
    contents = file.read()
    print(contents)


# Creating a File and Handling Binary File
# Example 4: Creating a new file (this will fail if the file already exists)
try:
    with open('file.txt', 'x') as file:
        file.write('This is a newly created file.')
except FileExistsError:
    print('File already exists')

# Example 5: Working with binary files (e.g., reading an image)
with open('image.png', 'rb') as file:
    binary_data = file.read()
#     Do something with the binary data


# Ensuring a File is Properly closed
# Example 6: Opening a file without using 'with' and ensuring it's closed
file = open('file.txt', 'r')
try:
    contents = file.read()
    print(contents)
finally:
    file.close()


# Using the 'with' Statement for Automatic Closing
# Example 7: Using 'with' for automatic closing (reading)
with open('example.txt', 'r') as file:
    contents = file.read()
    print(contents)

# Example 8: Using 'with' for automatic closing (writing)
with open('file.txt', 'w') as file:
    file.write('Writing to the file using with statement.')

# Example 9: Using 'with' for automatic closing (appending)
with open('file.txt', 'a') as file:
    file.write('\nAppending another line using with statement.')
