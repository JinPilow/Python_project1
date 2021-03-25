def calculat(s, a, b):
    if s == '*':
        return a * b
    elif s == '+':
        return a + b
    elif s == '-':
        return a - b
    else:
        return a / b


def issign(a):
    if a == '+' or a == '-' or a == '*' or a == '/':
        return 1
    else:
        return 0
