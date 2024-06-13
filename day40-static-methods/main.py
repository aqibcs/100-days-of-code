class Math:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def subtract(a, b):
        return a - b
    
    @staticmethod
    def multiply(a, b):
        return a * b
    
    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ValueError("cannot divide by zero.")
        return a / b

# Usage
print(Math.add(5, 3))
print(Math.subtract(5, 3))
print(Math.multiply(5, 3))
print(Math.divide(5, 3))