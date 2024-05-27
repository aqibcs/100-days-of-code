# Examples with Lists (Mutable Objects)
# Example 1: Comparing Lists with `==` and `is`
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True: They have the same values.
print(a is b)  # False: They are different objects in memory.


# Example 2: Comparing Identical Lists
a = [1, 2, 3]
b = a

print(a == b)  # True: They have the same values.
print(a is b)  # True: They are the same object in memory.


# Examples with Strings (Immutable Objects)
# Example 3: Comparing Strings with `==` and `is`
a = "hello"
b = "hello"

print(a == b)  # True: They have the same values.
print(a is b)  # True: They are the same object due to interning.


# Example 4: Comparing Longer Strings
a = "hello, world!"
b = "hello, world!"

print(a == b)  # True: They have the same values.
print(a is b)  # False: They may be different objects in memory (depends on interning).


# Examples with Integers (Immutable Objects)
# Example 5: Comparing Small Integers with == and is
a = 5
b = 5

print(a == b)  # True: They have the same values.
print(a is b)  # True: They are the same object due to interning.


# Example 6: Comparing Larger Integers
a = 1000
b = 1000

print(a == b)  # True: They have the same values.
print(a is b)  # False: They are different objects in memory.
