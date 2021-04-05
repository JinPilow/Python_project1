from tkinter import *
from lib.Math import *
from decimal import *

calculator = Tk()

calculator.title("계산기")
calculator.geometry("400x500+500+300")
calculator.resizable(False, False)

inputs = Entry(calculator, font=("Courier", 20))
inputs.grid(row=0, column=0, columnspan=4, sticky=W + E + S + N, pady=15, ipady=10)

btnStr = ["7", "8", "9", "*", "4", "5", "6", "/", "1", "2", "3", "=", "0", "+", "-", "AC", "C", ".", ""]

btns = []
for i in range(len(btnStr)):
    btns.append(Button(calculator, text=str(btnStr[i]), font=("Courier", 18), overrelief="solid", width=6, height=2,
                       command=lambda i=i: onclick(btnStr[i])))

count = 0
for i in range(1, 5):
    for j in range(0, 4):
        if count < 15:
            btns[count].grid(row=i, column=j, padx=2, pady=2)
            count += 1

for i in range(0, 4):
    btns[count].grid(row=5, column=i, padx=2, pady=2)
    count += 1

btns[11].grid(row=3, column=3, padx=2, rowspan=2, sticky=W + E + S + N, pady=2)


def onclick(text):
    if text == "=":
        calc(Entry.get(inputs))
    elif text == "AC":
        inputs.delete(0, END)
    elif text == "C":
        inputs.delete(len(Entry.get(inputs)) - 1, END)
    else:
        tinput = Entry.get(inputs) + text
        inputs.delete(0, END)
        inputs.insert(0, tinput)


def calc(s):
    str = s

    sign = []  # 부호 리스트
    number = []  # 숫자 리스트
    temp = ""  # 십의자리 이상 저장용
    if str[0] == "-":
        temp += str[0]
        str = str[1:]
    if str[0].isdigit():  # 숫자로 시작하는지 확인
        for i in range(len(str)):
            if str[i].isdigit() or str[i] == ".":  # 숫자확인후 temp에 저장
                temp += str[i]
            elif issign(str[i]):  # 부호일 경우 temp를 number에 저장하고 부호는 sign에 저장
                number.append(temp)
                temp = ""
                sign.append(str[i])
                if issign(str[i + 1]):
                    inputs.delete(0, END)
                    inputs.insert(0, "연산자가 연속으로 나옵니다!")
                    return
            else:  # 그 의외의 문자면 경고 출력후 프로그램 종료
                inputs.delete(0, END)
                inputs.insert(0, "숫자와 사칙연산만 입력해주세요!")
                print("숫자와 사칙연산만 입력해주세요!")
                return
            if i + 1 == len(str):  # 마지막 숫자 number에 저장
                number.append(temp)
    else:  # 예외처리
        inputs.delete(0, END)
        inputs.insert(0, "숫자로 시작해 주세요!")
        print("숫자로 시작해 주세요!")
        return

    count = 0  # 인덱스 변수
    while count < len(sign):
        if sign[count] == '*' or sign[count] == '/':  # 곱하기, 나누기 계산
            number[count] = calculat(sign[count], Decimal(number[count]), Decimal(number[count + 1]))
            del number[count + 1]
            del sign[count]
        else:
            count += 1  # 연산을 안햇을시 다음 인덱스, 안햇을시 인덱스 유지(계산된건 삭제되기 때문)

    count = 0
    while count < len(sign):
        if sign[count] == '+' or sign[count] == '-':  # 더하기, 빼기 계산
            number[count] = calculat(sign[count], Decimal(number[count]), Decimal(number[count + 1]))
            del number[count + 1]
            del sign[count]
        else:
            count += 1

    print("답은 : {}".format(number[0]))
    inputs.delete(0, "end")
    inputs.insert(0, number[0])


calculator.mainloop()
