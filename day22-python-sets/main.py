# Creating an empty Set
empty_set = set()
print(empty_set)

# Creating a set with values
fruits = {"apple", "banana", "cherry"}
print(fruits)

# Note:  Sets can also be created using the set() constructor
color = set(["red", "green", "blue"])
print(color)


#  Using union() and update() methods
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Using union() method
result_union = set1.union(set2)
print(result_union)

set3 = {6, 7}
set1.update(set3)
print((set1))


# Using intersection() and intersection_update() methods
set4 = {1, 2, 3, 4}
set5 = {3, 4, 5, 6}
# Using symmetric_difference() method
result_symmetric_diff = set4.symmetric_difference((set5))
print(result_symmetric_diff)

# Using symmetric_difference_update() method
set4.symmetric_difference_update(set5)
print(set4)


# Using difference() and difference_update() methods
set6 = {1, 2, 3, 4}
set7 = {3, 4, 5, 6}
# Using difference() method
result_difference = set6.difference(set7)
print(result_difference)

# Using difference_update() method
set6.difference_update(set7)
print(set6)


# Set Methods
# isdisjoint()
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set3 = {7, 8, 9}
print(set1.isdisjoint(set2))
print(set1.isdisjoint(set3))


# issuperset() and issubset()
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4}
set3 = {1, 2, 3, 4, 5, 6}
print(set1.issuperset(set2))
print(set1.issubset(set3))


# add(), update(), remove(), and discard()
set1 = {1, 2, 3}
set1.add(4)
print(set1)

set2 = {4, 5, 6}
set1.update(set2)
print(set1)

set1.remove(6)
print(set1)

set1.discard(2)
print(set1)


# pop(), clear(), del
set1 = {1, 2, 3, 4, 5}
popped_item = set1.pop()
print(set1)
print(popped_item)

set1.clear()
print(set1)

set2 = {1, 2, 3}
del set2
# print(set2) # This would raise a NameError since set2 has been deleted


# Checking item existing
fruits = {"apple", "banana", "cherry"}
if "banana" in fruits:
    print("Yes, banana is in the fruits set.")

if "orange" not in fruits:
    print("No, orange is not in the fruits set.")