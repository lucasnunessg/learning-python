PI = 3.14


def square(side):
    """calculate area of square."""
    return side * side


def rectangle(length, width):
    """Calculate area of rectangle"""
    return length * width


def circle(radius):
    """calculate area of circle"""
    return PI * radius * radius


print("Área do quadrado:", square(10))
print("Área do retângulo:", rectangle(2, 2))
print("Área do círculo:", circle(3))
