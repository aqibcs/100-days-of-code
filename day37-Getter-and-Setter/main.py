class MyClass:
    def __init__(self, value) -> None:
        self.value = value
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        if new_value < 0:
            raise ValueError("Value must be non-negative")
        self._value = new_value


obj = MyClass(10)
print(obj.value)

obj.value = 20
print(obj.value)

try:
    obj.value = -5
except ValueError as e:
    print(e)