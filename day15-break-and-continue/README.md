# break statement
The `break` statement is used to exit or "break" out of a loop prematurely. When encountered, it immediately terminates the loop it's inside, regardless of whether the loop's conditions have been fully met or not. This can be useful for stopping a loop early based on certain conditions being met.
## Example:
```python
for i in range(1, 101):
    print(i, end=" ")
    if i == 50:
        break
print("Thank you")
```

# Continue Statement
The `continue` statement is used to skip the current iteration of a loop and move to the next iteration. It's useful when you want to skip certain elements or conditions within a loop without terminating the entire loop.
## Example:
```python
for i in range(1, 11):
    if i % 2 != 0:
        continue
    print(i)
```