
formula = []

while True:
    term = input("계산식을 입력하시오")
    if term == "=":
        break
    formula.append(term)
    if formula[0].isnumeric() == False:
        print("잘못된 식입니다.")
        quit()
    for i in range(len(formula)):
        if formula[i].isnumeric == False and formula[i+1].isnumeric == False:
            print("잘못된 식입니다.")

print(formula)

from lib.Math import *
'''
i = 0
for i in range(len(formula)-1):
    if '*' in formula or '/' in formula:
        j = 0
        while j < len(formula)-1:
            if formula[j] == '*':
                formula[j] = mul(float(formula[j-1]), float(formula[j+1]))
                print(formula)
                formula.remove(formula[j+1])
                formula.remove(formula[j-1])
                print(formula)
            elif formula[j] == '/':
                formula[j] = div(float(formula[j-1]), float(formula[j+1]))
                formula.remove(formula[j+1])
                formula.remove(formula[j-1])
                print(formula)
            else:
                j += 1

    else:
        j = 0
        while j < len(formula)-1:
            if formula[j] == '+':
                formula[j] = add(float(formula[j-1]), float(formula[j+1]))
                formula.remove(formula[j+1])
                formula.remove(formula[j-1])
                print(formula)
            elif formula[j] == '-':
                formula[j] = sub(float(formula[j-1]), float(formula[j+1]))
                formula.remove(formula[j+1])
                formula.remove(formula[j-1])
                print(formula)
            else:
                j += 1
print(formula)
'''

for i in range(len(formula)):
    if '*' in formula or '/' in formula:
        while len(formula) > 1:
            if formula[i] == '*':
                formula[i] = mul(float(formula[i - 1]), float(formula[i + 1]))
                print(formula)
                formula.remove(formula[i + 1])
                print(formula)
                formula.remove(formula[i - 1])
                print(formula)
            elif formula[i] == '/':
                formula[i] = div(float(formula[i - 1]), float(formula[i + 1]))
                print(formula)
                formula.remove(formula[i + 1])
                print(formula)
                formula.remove(formula[i - 1])
                print(formula)
            else:
                i += 1
    else:
        while len(formula) > 1:
            if formula[i] == '+':
                formula[i] = add(float(formula[i - 1]), float(formula[i + 1]))
                print(formula)
                formula.remove(formula[i + 1])
                print(formula)
                formula.remove(formula[i - 1])
                print(formula)
            elif formula[i] == '-':
                formula[i] = sub(float(formula[i - 1]), float(formula[i + 1]))
                print(formula)
                formula.remove(formula[i + 1])
                print(formula)
                formula.remove(formula[i - 1])
                print(formula)
            else:
                i += 1




'''
j = 0
while j < len(formula)-1:
    if formula[j] == '*':
        formula[j] = mul(float(formula[j-1]), float(formula[j+1]))
        print(formula)
        formula.remove(formula[j+1])
        formula.remove(formula[j-1])
        print(formula)
    elif formula[j] == '/':
        formula[j] = div(float(formula[j-1]), float(formula[j+1]))
        formula.remove(formula[j+1])
        formula.remove(formula[j-1])
        print(formula)
    else:
        j += 1
    if len(formula)-1 == 1:
        break

print(formula)
'''
'''
if type(formula) == 'int':
    int(formula)
'''
'''
for i in range(len(formula)):
    if '*' in formula:
        sign = formula.index("*")
        formula[sign] = mul(int(formula[sign-1]), int(formula[sign+1]))
        formula.remove(formula[sign+1])
        formula.remove(formula[sign-1])
        print(formula)
    elif '/' in formula:
        sign = formula.index("/")
        formula[sign] = div(int(formula[sign-1]), int(formula[sign+1]))
        formula.remove(formula[sign+1])
        formula.remove(formula[sign-1])
        print(formula)
    elif '-' in formula:
        sign = formula.index("-")
        formula[sign] = sub(int(formula[sign-1]), int(formula[sign+1]))
        formula.remove(formula[sign+1])
        formula.remove(formula[sign-1])
        print(formula)
    elif '+' in formula:
        sign = formula.index("+")
        formula[sign] = add(int(formula[sign-1]), int(formula[sign+1]))
        formula.remove(formula[sign+1])
        formula.remove(formula[sign-1])
        print(formula)
    else:
        pass
print("Result: {}".format(formula))
'''