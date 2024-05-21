# Script with multiple function
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def main():
    print("Running script directly")
    result = add(5, 3)
    print("Addition result: ", result)


if __name__ == "__main__":
    main()



# Script with class definitions:
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b


def main():
    calc = Calculator()
    result = calc.subtract(10, 5)
    print("Subtract result: ", result)


if __name__ == "__main__":
    main()