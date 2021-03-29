def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def calc(formula, sign, i):
    if sign == '*':
        formula[i] = mul(int(formula[i - 1]), int(formula[i + 1]))
    elif sign == '/':
        formula[i] = div(int(formula[i - 1]), int(formula[i + 1]))
    elif sign == '+':
        formula[i] = add(int(formula[i - 1]), int(formula[i + 1]))
    elif sign == '-':
        formula[i] = sub(int(formula[i - 1]), int(formula[i + 1]))
    del formula[i + 1]
    del formula[i - 1]
    return formula