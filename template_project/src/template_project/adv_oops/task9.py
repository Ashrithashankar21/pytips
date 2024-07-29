from abc import ABC, abstractmethod
import math


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius**2)

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        # Using Heron's formula
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c


circle = Circle(radius=5)
rectangle = Rectangle(width=4, height=6)
triangle = Triangle(a=3, b=4, c=5)

print(f"Circle: Area = {circle.area():.2f}, Perimeter = {circle.perimeter():.2f}")
print(
    f"Rectangle: Area = {rectangle.area():.2f}, Perimeter = {rectangle.perimeter():.2f}"
)
print(f"Triangle: Area = {triangle.area():.2f}, Perimeter = {triangle.perimeter():.2f}")
