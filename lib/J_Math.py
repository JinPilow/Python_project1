def calculat(s, a, b):
    if s == '*':
        return a * b
    elif s == '+':
        return a + b
    elif s == '-':
        return a - b
    else:
        return a / b


def function1(str, count):
    str[count - 1] = calculat(str[count], float(str[count - 1]), float(str[count + 1]))
    del str[count]
    del str[count]
    return str


def function2(str, count):
    str[count - 1] = calculat(str[count], float(str[count - 1]), float(str[count + 1]))
    del str[count]
    del str[count]
    return str


def issign(a):
    if a == '+' or a == '-' or a == '*' or a == '/':
        return 1
    else:
        return 0
