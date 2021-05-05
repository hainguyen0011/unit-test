from quadratic_equation import delta_calculator, solve


def main():
    try:
        a = int(input('enter a: '))
        b = int(input('enter b: '))
        c = int(input('enter c: '))
        a, b, c = convertor(a, b, c)
        print()
        if a == 0:
            print('invalid equation')
        else:
            delta = delta_calculator(a, b, c)
            if delta > 0:
                x1, x2 = solve(a, b, delta)
                print('x1 = {0}\nx2 = {1}'.format(x1, x2))
            elif delta == 0:
                x = solve(a, b, delta)
                print('x = {0}'.format(x))
            else:
                real_part, imaginary_part = solve(a, b, delta)
                if real_part == 0:
                    print('x1 = {0}i\nx2 = -{0}i'.
                          format(imaginary_part))
                else:
                    print('x1 = {0} + {1}i\nx2 = {0} - {1}i'.
                          format(real_part, imaginary_part))
    except ValueError:
        print('coefficients must be a number')


def convertor(*args):
    for i in args:
        i = int(i)
        yield i


if __name__ == '__main__':
    main()
