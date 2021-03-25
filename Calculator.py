
a = []

for i in range(1,100):
    b = input("계산식을 입력하시오")
    if b == "=":
        break
    else:
        a.append(b)
print(a)

from lib.Math import *

for i in range(len(a)):
    if '*' in a:
        b = a.index("*")
        a[b] = mul(int(a[b-1]), int(a[b+1]))
        a.remove(a[b+1])
        a.remove(a[b-1])
    elif '/' in a:
        b = a.index("/")
        a[b] = div(int(a[b-1]), int(a[b+1]))
        a.remove(a[b+1])
        a.remove(a[b-1])
    elif '-' in a:
        b = a.index("-")
        a[b] = sub(int(a[b-1]), int(a[b+1]))
        a.remove(a[b+1])
        a.remove(a[b-1])
    elif '+' in a:
        b= a.index("+")
        a[b] = add(int(a[b-1]), int(a[b+1]))
        a.remove(a[b+1])
        a.remove(a[b-1])
    else:
        pass

print("Result: {}".format(a))
