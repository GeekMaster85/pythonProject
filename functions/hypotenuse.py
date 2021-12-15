import math


def hypotenuse(x, y):
    return math.sqrt(x ** 2 + y ** 2)


print(hypotenuse(3, 4))


def is_between(x, y, z):
    return x <= y <= z


print(is_between(2, 3, 5))
