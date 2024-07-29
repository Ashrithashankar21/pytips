class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def __str__(self):
        return f"({self.real} + {self.img}i)"

    def __add__(self, other):
        return Complex(self.real + other.real, self.img + other.img)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.img - other.img)

    def __mul__(self, other):
        real_part = self.real * other.real - self.img * other.img
        img_part = self.real * other.img + self.img * other.real
        return Complex(real_part, img_part)

    def __truediv__(self, other):
        denom = other.real**2 + other.img**2
        real_part = (self.real * other.real + self.img * other.img) / denom
        img_part = (self.img * other.real - self.real * other.img) / denom
        return Complex(real_part, img_part)

    def __eq__(self, other):
        return self.real == other.real and self.img == other.img


if __name__ == "__main__":
    c1 = Complex(3, 2)
    c2 = Complex(1, 7)

    print(f"c1: {c1}")
    print(f"c2: {c2}")

    print(f"c1 + c2 = {c1 + c2}")

    print(f"c1 - c2 = {c1 - c2}")

    print(f"c1 * c2 = {c1 * c2}")

    print(f"c1 / c2 = {c1 / c2}")

    c3 = Complex(3, 2)
    print(f"c1 == c3: {c1 == c3}")
    print(f"c1 == c2: {c1 == c2}")
