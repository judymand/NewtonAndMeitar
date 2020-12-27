import math

def Newton_Raphson(f, d, a, b, eps):
    # f=function
    # d=derived

    # no root between two points
    if f(a) * f(b) > 0:
        return

    xr = (a + b) / 2
    xr1 = xr + eps
    count = 0

    while abs(xr - xr1) > eps:
        count = count + 1
        xr = xr1
        xr1 = xr - f(xr) / d(xr)

    print(count, "iteration to find root (", xr, ", 0 )")
    return


def secant_method(f, xn_1, xn, eps):
    d = 2 * eps  # first guess
    count = 0
    while abs(d) > eps:
        count = count + 1
        d = (xn - xn_1) / (f(xn) - f(xn_1)) * f(xn)
        xn_1 = xn
        xn = xn - d

    print(count, "iteration to find root (", xn, ", 0 )")
    return


if __name__ == '__main__':
    eps = 0.0001
    print("~~~ NEWTON METHOD ~~~")
    print("function: x**2-6")
    for i in range(-5, 5):
        Newton_Raphson(lambda x: x ** 2 - 6, lambda x: 2 * x, i, i + 1, eps)
    print("------------------------")
    print("function: x**4+8*x**3+4*x**2")
    for i in range(-8, 1):
        Newton_Raphson(lambda x: x ** 4 + 8 * x ** 3 + 4 * x ** 2, lambda x: 4 * x ** 3 + 24 * x ** 2 + 8 * x, i, i + 1, eps)
    print("~~~ MEITAR METHOD ~~~")
    print("function: x**3 -math.cos(x)")
    secant_method(lambda x: x ** 3 - math.cos(x), 1, 2, eps)
