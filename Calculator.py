
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
