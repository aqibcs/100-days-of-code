# Creating a string with single quotes:
name = 'Aqib'
print("Hello, " + name)

# Creating a string with double quotes:
sentence = "He said, \"I want to eat an apple\"."
print(sentence)

# Creating a multi-line string using triple quotes:
multi_line_string = """
This is a multi-line string
that spans across multiple lines
in Python.
You can use triple quotes
to define such strings easily.
"""
print(multi_line_string)

# String Concatenation:
greeting = "Hello"
name = "Aqib"
message = greeting + ", " + name + "!"
print(message)  # Output: Hello, Aqib!

# String Length:
sentence = "Python is amazing!"
length = len(sentence)
print("Length of the sentence:", length)  # Output: Length of the sentence: 18

# String Slicing:
sentence = "Hello, World!"
substring = sentence[7:12]
print(substring)  # Output: World

# String Methods:
sentence = "hello, world"
upper_case = sentence.upper()  # Convert to uppercase
lower_case = sentence.lower()  # Convert to lowercase
title_case = sentence.title()  # Convert to title case
print(upper_case)  # Output: HELLO, WORLD
print(lower_case)  # Output: hello, world
print(title_case)  # Output: Hello, World

# String Splitting:
sentence = "Python,Java,C++,JavaScript"
languages = sentence.split(',')
print(languages)  # Output: ['Python', 'Java', 'C++', 'JavaScript']

# String Joining:
languages = ['Python', 'Java', 'C++', 'JavaScript']
sentence = ', '.join(languages)
print(sentence)  # Output: Python, Java, C++, JavaScript
