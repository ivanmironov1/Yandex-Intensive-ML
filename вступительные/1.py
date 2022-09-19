import math

func = input()
d = int(input())


def fun(x):
    if func[:3] == 'sin':
        if func[3] == '(':
            return 7 * math.cos(x)
        a = int(func[4])
        return 7 * a * math.cos(7 * x) * (math.sin(7 * x) ** (a - 1))

    elif func[:-1] == 'x^':
        if func[-1] == 'x':
            return 1
        a = int(func[-1])
        return a * x ** (a - 1)

    elif func[:5] == '(2-x)':
        if func[-1] == ')':
            return - (2 - x) / (x + 1) ** 2 - 1 / (x + 1)
        a = int(func[-1])
        return -a * (2 - x) / (x + 1) ** (a + 1) - 1 / (x + 1) ** a


print(fun(d))
