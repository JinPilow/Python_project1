def calculat(s, a, b):
    if s == '*':
        return a * b
    elif s == '+':
        return a + b
    elif s == '-':
        return a - b
    else:
        return a / b


def calculat2(s, str, i):
    if s == '*':
        if str[i] == '*':
            str[i - 1] = int(str[i - 1]) * int(str[i + 1])
    elif s == '/':
        if str[i] == '/':
            str[i - 1] = int(str[i - 1]) / int(str[i + 1])
    elif s == '+':
        if str[i] == '+':
            str[i - 1] = int(str[i - 1]) + int(str[i + 1])
    elif s == '-':
        if str[i] == '-':
            str[i - 1] = float(str[i - 1]) - float(str[i + 1])
    del str[i]
    print(i)
    del str[i]
    return str


def issign(a):
    if a == '+' or a == '-' or a == '*' or a == '/':
        return 1
    else:
        return 0
