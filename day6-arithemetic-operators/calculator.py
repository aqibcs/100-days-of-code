def switch(operator, num1, num2):
    match operator:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            return num1 / num2

num1 = float(input("Enter firsr number: "))
operator = input("Enter operator (+ - * /): ")
num2 = float(input("Enter another number: "))

result = switch(operator, num1, num2)
print(result)