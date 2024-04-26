# Day-3: Module and pip in Python!
Module is like a code library which can be used to borrow code written by somebody else in our python program. There are two types of modules in python:

1. Built in Modlues - These modules are ready to import and use and ships with the python interpreter. there is no need to install such modules explicity.
2. External Modules - These modules are imported from a third party file or can be install using a package manager like pip or conda. Since this code is written by someone else. we can install different versions of a same module with time.

## The pip command
it can be used as a package manager **pip** to install a python module. Lets install a module called pandas using the following command

```bash
pip install pandas
```

## Using a module in Python (Usage)
We use the import syntax to import a module in Python. Here is an example code:
```python
import pandas

# Read and work with a file named 'words.csv'
df = pandas.read_csv('words.csv')
print(df) # This will display first few rows from the words.csv file
```
