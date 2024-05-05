count = 5
while (count > 0):
    print(count)
    count = count - 1


# Using Else with While Loop
count = 0
while count < 10:
    if count % 2 == 0:
        print(count, "is even")
    else:
        print(count, "is odd")
    count += 1
else:
    print("Loop ended, count is", count)


# Emulating Do-While Loop
while True:
    try:
        num = int(input("Enter a positive number: "))
        if num > 0:
            print("Valid input:", num)
            break
        else:
            print("Please enter a positive number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")