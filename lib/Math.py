from decimal import Decimal

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
        formula[i] = mul(Decimal(formula[i - 1]), Decimal(formula[i + 1]))
    elif sign == '/':
        formula[i] = div(Decimal(formula[i - 1]), Decimal(formula[i + 1]))
    elif sign == '+':
        formula[i] = add(Decimal(formula[i - 1]), Decimal(formula[i + 1]))
    elif sign == '-':
        formula[i] = sub(Decimal(formula[i - 1]), Decimal(formula[i + 1]))
    del formula[i + 1]
    del formula[i - 1]
    return formula

a = "python"
