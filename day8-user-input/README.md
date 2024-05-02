# Day-8: Taking User Input in Python
In python, we can take user input directly by using input() function. This input function gives a return value as string/character hence we have to pass that into a variable.

## Syntax:
```python
variable = input()
```
But input function returns the value as string. Hence we have to typecast them whenever required to another datatype.

## Example:
```python
variable = int(input())
variable = float(input())
```
We can also display a text input function. This will make input() function take user input and display a message as well.

## Example:
```python
a = input("Enter the name: ")
print(a)
```

## Output:
```bash
Enter the name: Aqib
Aqib
```