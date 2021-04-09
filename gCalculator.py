from tkinter import *
from lib.Math import *
from decimal import *

calculator = Tk()

calculator.title("계산기")
calculator.geometry("400x500+500+300")
calculator.resizable(False, False)

inputs = Entry(calculator, font=("Courier", 20))
inputs.grid(row=0, column=0, columnspan=4, sticky=W + E + S + N, pady=15, ipady=10, padx=5)

btnStr = ["7", "8", "9", "*", "4", "5", "6", "/", "1", "2", "3", "=", "0", "+", "-", "AC", "C", ".", "00"]

btns = []
restart = False     # 재입력 스위치
for i in range(len(btnStr)):    # 버튼생성 및 이벤트 연결
    btns.append(Button(calculator, text=str(btnStr[i]), font=("Courier", 18), overrelief="solid", width=6, height=2,
                       command=lambda i=i: onclick(btnStr[i])))

count = 0
for i in range(1, 5):       # 버튼 배치
    for j in range(0, 4):
        if count < 15:
            btns[count].grid(row=i, column=j, padx=2, pady=2)
            count += 1

for i in range(0, 4):       # 마지막줄 버튼 배치
    btns[count].grid(row=5, column=i, padx=2, pady=2)
    count += 1

# = 버튼 크기 변경
btns[11].grid(row=3, column=3, padx=2, rowspan=2, sticky=W + E + S + N, pady=2)


def onclick(text):  # 버튼 이벤트
    global restart  # 재입력 스위치
    if text == "=":
        calc(Entry.get(inputs))     # 계산함수
        restart = True
    elif text == "AC":
        inputs.delete(0, END)
    elif text == "C":
        inputs.delete(len(Entry.get(inputs)) - 1, END)
    elif restart and text.isdigit():    # 재입력 상태에서 숫자를 입력했을때 재입력
        inputs.delete(0, END)
        inputs.insert(0, text)
        restart = False
    else:                               # 아니라면 (재입력 상태에서 부호가 입력) 초기화 없이 계속 입력
        tinput = Entry.get(inputs) + text
        inputs.delete(0, END)
        inputs.insert(0, tinput)
        restart = False


def calc(s):
    str = s

    # 식 앞에는 0+ 가 추가된 상태로 시작한다
    sign = ["+"]  # 부호 리스트
    number = ["0"]  # 숫자 리스트
    temp = ""  # 십의자리 이상 저장용
    if str[0] == "-":   # 첫 입력이 - 일 경우
        del sign[0]
        sign.append("-")    # 앞에 0- 로 바꾼다
        str = str[1:]
    elif str[0] == "+":     # 그대로 삭제
        str = str[1:]

    try:
        if str[0].isdigit():  # 숫자로 시작하는지 확인
            i = 0
            while i < len(str):
                if str[i].isdigit() or str[i] == ".":  # 숫자 혹은 점 확인후 temp에 저장
                    temp += str[i]
                    i += 1
                elif issign(str[i]):  # 부호일 경우 temp를 number에 저장하고 부호는 sign에 저장
                    number.append(temp)
                    temp = ""
                    sign.append(str[i])
                    if issign(str[i + 1]):  # 다음이 부호가 + - 일 경우 temp에 부호 보내기
                        if str[i+1] == "-" or str[i+1] == "+":  # 연속된 부호중 뒤의 부호가 + - 일 경우 그 부호를 다음 수에 합치기
                            temp += str[i+1]
                            i += 1
                        else:
                            inputs.delete(0, END)
                            inputs.insert(0, "잘못된 연산자가 연속으로 나옵니다!")
                            return
                    i += 1
                if i == len(str):  # 마지막 숫자 number에 저장
                    number.append(temp)
        else:  # 예외처리
            inputs.delete(0, END)
            inputs.insert(0, "숫자로 시작해 주세요!")
            return

        # 곱하기, 나누기 계산
        count = 0  # 인덱스 변수
        while count < len(sign):
            if sign[count] == '*' or sign[count] == '/':
                number[count] = calculat(sign[count], Decimal(number[count]), Decimal(number[count + 1]))
                del number[count + 1]
                del sign[count]
            else:
                count += 1  # 연산을 안햇을시 인덱스 유지(계산된건 삭제되기 때문)

        # 더하기, 빼기 계산
        count = 0
        while count < len(sign):
            print(number)
            print(sign)
            if sign[count] == '+' or sign[count] == '-':
                number[count] = calculat(sign[count], Decimal(number[count]), Decimal(number[count + 1]))
                del number[count + 1]
                del sign[count]
            else:
                count += 1

        print("답은 : {}".format(number[0]))
        inputs.delete(0, "end")
        inputs.insert(0, number[0])

    except (IndexError, InvalidOperation):
        inputs.delete(0, END)
        inputs.insert(0, "잘못된 식을 입력 했습니다!")


calculator.mainloop()