class Point:

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Point(self.x * other.x, self.y * other.y)

    def __truediv__(self, other):
        return Point(self.x / other.x, self.y / other.y)

    def __lt__(self, other):
        return Point(self.x < other.x, self.y < other.y)

    def __gt__(self, other):
        return Point(self.x > other.x, self.y > other.y)

    def __eq__(self, other):
        return Point(self.x == other.x, self.y == other.y)

    def __str__(self):
        return f"Point({self.x}, {self.y})"


# Example of using the Point class with operator overloading
p1 = Point(1, 2)
p2 = Point(3, 4)

# Add two points
p3 = p1 + p2
print(p3)

# Subtract two points
p4 = p1 - p2
print(p4)

# Multiply two points
p5 = p1 * p2
print(p5)

# Divide two points
p6 = p1 / p2
print(p6)

# Comparison of two points
print(p1 < p2)
print(p1 > p2)
print(p1 == p2)

# Equality check
p7 = Point(1, 2)
print(p1 == p7)
