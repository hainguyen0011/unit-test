from quadratic_equation import delta_calculator, solve


def main():
    a = int(input('enter a: '))
    b = int(input('enter b: '))
    c = int(input('enter c: '))
    delta = delta_calculator(a, b, c)
    if delta > 0:
        x1, x2 = solve(a, b, c, delta)
        print('x1 = {0}\nx2 = {1}'.format(x1, x2))
    elif delta == 0:
        x = solve(a, b, c, delta)
        print('x = {0}'.format(x))
    else:
        real_part, imaginary_part = solve(a, b, c, delta)
        print(
            'x1 = {0} + {1}i\nx2 = {0} - {1}i'.format(real_part, imaginary_part))


if __name__ == 'main':
    main()
