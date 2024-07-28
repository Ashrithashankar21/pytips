import math
from typing import Tuple


def solve_quad(a: float, b: float, c: float) -> Tuple[float, float]:
    # Calculate the discriminant
    discriminant = b**2 - 4 * a * c

    # Check if the discriminant is negative, zero, or positive
    if discriminant < 0:
        raise ValueError("The equation has no real roots")
    elif discriminant == 0:
        # One real root (both solutions are the same)
        x = -b / (2 * a)
        return (x, x)
    else:
        # Two distinct real roots
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return (x1, x2)


if __name__ == "__main__":
    a, b, c = 1, -3, 2
    x1, x2 = solve_quad(a, b, c)
    print(f"{x1} and {x2}")
