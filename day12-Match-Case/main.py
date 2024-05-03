# Define the variable fruit
fruit = "apple"

# Match the variable fruit using match case
match fruit:
    case "apple":
        print("It's an apple!")
    case "banana":
        print("It's a banana!")
    case "orange":
        print("It's an orange!")
    case _:
        print("Unknown fruit!")