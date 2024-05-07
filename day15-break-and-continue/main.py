# Break Statement:
# Breaking out of a loop in a range:
for i in range(1, 101):
    print(i, end=" ")
    if i == 50:
        break
print("Thank you")

# Breaking out of a while loop:
num = 0
while num < 10:
    print(num)
    if num == 5:
        break
    num += 1


# Continue Statement:
# Skipping odd numbers in a loop:
for i in range(1, 11):
    if i % 2 != 0:
        continue
    print(i)

# Skipping specific elements in a list:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num == 5 or num == 7:
        continue
    print(num)