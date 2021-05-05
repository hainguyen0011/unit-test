from math import sqrt


def delta_calculator(a, b, c):
    delta = b*b - 4*a*c
    return delta


def solve(a, b, delta):
    if delta > 0:
        x1 = (-b + sqrt(delta)) / (2*a)
        x2 = (-b - sqrt(delta)) / (2*a)
        return x1, x2
    elif delta == 0:
        x = -b/(2*a)
        return x
    else:
        real_part = round(-b / (2*a), 3)
        imaginary_part = round(sqrt(-delta) / (2*a), 3)
        return real_part, imaginary_part
