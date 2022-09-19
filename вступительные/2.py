import math

m, n = map(int, input().split())


def fac(x):
    if x == 0:
        return 1
    return math.factorial(x - 1) * x


def C(a, b):
    return math.factorial(a) / (math.factorial(b) * math.factorial(a - b))


print(int(C(m + n, 3) - C(m, 3) - C(n, 3)))
