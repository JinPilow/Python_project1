from tkinter import *
from tkinter import messagebox
from lib.Math import *

class Main:
    def __init__(self, tk):
        self.calc = Function()

class Interface():
    def layout(self):
        self.entry = Entry(upper_frame, justify = "right", width=20, font=("Courier", 18), borderwidth=5)
        self.entry.pack()
        self.entry.insert(0, "0")

        # 숫자 버튼 설정
        bnum = []
        for number in range(10):  # 숫자 버튼 1~9 생성
            button_num = Button(down_frame, text=str(number), font=("Courier", 18), padx=15, pady=10,
                             command=lambda number=number: self.click(number))
            bnum.append(button_num)
        bnum.append(Button(down_frame, text="00", font=("Courier", 18), padx=9, pady=10,
                           command=lambda: self.click('00')))  # 숫자 버튼 00 생성
        bnum.append(Button(down_frame, text=".", font=("Courier", 18), padx=15, pady=10,
                           command=lambda: self.click('.')))  # 숫자 버튼 소수점 '.' 생성

        countnum = 1
        for row in range(3):  # 숫자 버튼 gui 위치 지정
            for column in range(3):
                bnum[countnum].grid(row=2 - row, column=column, padx=5, pady=5)
                countnum += 1

        bnum[0].grid(row=3, column=1, padx=5, pady=5)
        bnum[10].grid(row=3, column=0, padx=5, pady=5)
        bnum[11].grid(row=3, column=2, padx=5, pady=5)

        # 부호 버튼 설정
        bsign = []
        for sign in ["*", "/", "+", "-"]:  # 부호 버튼 "*","/","+","-" 생성
            button_sign = Button(down_frame, text=sign, font=("Courier", 18), padx=15, pady=10,
                             command=lambda sign=sign: self.click(sign))
            bsign.append(button_sign)

        bsign.append(Button(down_frame, text="=", font=("Courier", 18), padx=15, pady=10,
                            command=lambda: self.equal()))  # 부호 버튼 "=" 생성
        bsign.append(Button(down_frame, text="C", font=("Courier", 18), padx=15, pady=10,
                            command=lambda: self.clear()))  # 부호 버튼 클리어 "C" 생성
        bsign.append(Button(down_frame, text="AC", font=("Courier", 18), padx=8, pady=10,
                            command=lambda: self.all_clear()))  # 부호 버튼 올클리어 "AC" 생성
        bsign.append(Button(down_frame, text="+/-", font=("Courier", 18), padx=2, pady=10,
                            command=lambda: self.switch_sign()))  # 부호 버튼 부호 변환 "+/-" 생성

        countsign = 0
        for row in range(5):  # 부호 버튼 gui 위치 지정
            bsign[countsign].grid(row=row, column=3, padx=5, pady=5)
            countsign += 1

        bsign[4].grid(row=4, column=3, padx=5, pady=5)
        bsign[5].grid(row=4, column=2, padx=5, pady=5)
        bsign[6].grid(row=4, column=1, padx=5, pady=5)
        bsign[7].grid(row=4, column=0, padx=5, pady=5)

class Function(Interface):
    def __init__(self):
        self.layout()
        self.count = 0
        self.result = True

    # 클릭 함수 생성
    def click(self, n):
        if self.result and str(n).isdigit():  # 첫 입력 또는 "=" 입력 후 다음 계산식 입력할 때 entry의 값을 지우고 해당 숫자 입력
            self.entry.delete(0, END)
            self.count = 0
        current = self.entry.get()
        if self.result and str(n) == ".":
            if current == "0":  # 첫 입력 또는 "=" 입력 후 "." 입력할 때 entry에 "0." 출력
                self.entry.delete(0, END)
                self.entry.insert(0, "0.")
                self.result = False
            else:
                self.entry.delete(0, END)
                self.entry.insert(0, str(current) + str(n))
                self.result = False
        elif self.result and current == "0":  # 첫 입력 또는 "=" 입력 후 부호 입력할 때 entry에서 초기값 0을 지우고 부호만 출력
            self.entry.delete(0, END)
            self.entry.insert(0, str(n))
            self.result = False
        elif self.result and str(n) in ["00", "0"]:  # 첫 입력 또는 "=" 입력 후 "00" 또는 "0" 입력할 때 entry에 0만 출력
            self.count = 0
            self.entry.insert(0, "0")
            self.result = True
        else:
            self.entry.delete(0, END)
            self.entry.insert(0, str(current) + str(n))
            self.result = False
        if self.entry.get() == "0.":
            self.count = 1
        if str(n) == "00":
            self.count += 2
        elif str(n).isdigit() or str(n) == ".":
            self.count += 1
        else:
            self.count = 0

    # 클리어 함수 생성
    def clear(self):
        current = self.entry.get()
        current = current[:-1]
        self.entry.delete(0, END)
        self.entry.insert(0, current)
        self.count -= 1
        if len(current) == 0:
            self.entry.insert(0, "0")
            self.count = 0

    # 올클리어 함수 생성
    def all_clear(self):
        self.entry.delete(0, END)
        self.entry.insert(0, "0")
        self.result = True

    # 부호 변환 함수 생성
    def switch_sign(self):
        current = self.entry.get()
        temp = current[-self.count - 1:]
        if not temp[0].isdigit():
            if len(temp) == 1:
                messagebox.showerror("Error", "기능을 수행할 수 없습니다.")
            if temp[0] in ["+", "-"]:
                if float(temp) < 0:
                    current = current[:-self.count - 1] + "+" + current[-self.count:]
                elif float(temp) > 0:
                    current = current[:-self.count - 1] + "-" + current[-self.count:]
            else:
                if float(temp[1:]) < 0:
                    current = current[:-self.count:] + "+" + current[-self.count:]
                elif float(temp[1:]) > 0:
                    current = current[:-self.count:] + "-" + current[-self.count:]
                else:
                    current = 0
        else:
            if float(temp) < 0:
                current = current.replace(current[-self.count:], "+" + current[-self.count:])
            elif float(temp) > 0:
                current = current.replace(current[-self.count:], "-" + current[-self.count:])
            else:
                current = 0

        self.entry.delete(0, END)
        self.entry.insert(0, current)

    # 등호(계산) 함수 생성
    def equal(self):
        current = self.entry.get()
        formula = []
        temp = ""
        i = 0

        if len(current) == 1:
            if current[0].isdigit():
                formula.append(current[0])
            else:
                messagebox.showerror("Error", "연산을 수행할 수 없습니다.")
        else:
            if current[0] == "-":                       # 계산식 첫 글자가 "-"일 때 배열에 "0", "-"를 추가하여 음수로 연산
                formula.extend(["0", "-"])
                i = 1
            elif current[0] == "+":                     # 계산식 첫 글자가 "+"일 때 배열에 "0", "+"를 추가하여 양수로 연산
                formula.extend(["0", "+"])
                i = 1
            elif not current[0].isdigit():              # 계산식 첫 글자가 그 외의 문자일 때 에러 메세지 출력
                messagebox.showerror("Error", "연산을 수행할 수 없습니다.")

            while True:
                if is_digit(current[i]):                # 첫번째 이외 글자가 숫자이거나 소수점일 때 문자열에 저장
                    temp += current[i]
                    i += 1
                elif not current[i].isdigit():          # 첫번째 이외 글자가 부호일 때 문자열에 저장된 숫자들을 배열에 추가하고 부호도 배열에 추가
                    if current[i + 1] in ["+", "-"]:    # 부호 두 개 연달아 입력시 나중에 입력된 부호가 "+" 또는 "-"일 경우 문자열에 숫자와 함께 저장
                        formula.append(temp)
                        formula.append(current[i])
                        temp = ''
                        temp += current[i + 1]
                        i += 2
                    elif current[i + 1] in ["*", "/"]:  # 부호 두 개 연달아 입력시 나중에 입력된 부호가 "*" 또는 "/"일 경우 오류 메세지 출력
                        i += 1
                        messagebox.showerror("Error", "잘못된 연산자입니다.")
                        self.entry.delete(0, END)
                    elif current[i] == ".":
                        temp += current[i]
                        i += 1
                    else:
                        formula.append(temp)
                        formula.append(current[i])
                        temp = ''
                        i += 1
                if i == len(current) - 1:               # 마지막 숫자를 배열에 저장
                    temp += current[i]
                    formula.append(temp)
                    self.result = True
                    break
                # for component in range(len(formula)):
                #     if component % 2 == 0:
                #         if not is_digit(formula[component]):
                #             messagebox.showerror("Error", "연산을 수행할 수 없습니다.")
                #             self.entry.delete(0, END)

        i = 0
        while len(formula) > 1:
            if '*' in formula or '/' in formula:        # 곱셈, 나눗셈 우선 계산
                if formula[i] == '*':                   # i 번째 입력값이 곱셈일 경우 calc 함수를 실행하고 i 값을 초기화, 루프를 다시 실행
                    calc(formula, '*', i)
                    i = 0
                elif formula[i] == '/':                 # i 번째 입력값이 나눗셈일 경우 calc 함수를 실행하고 i 값을 초기화, 루프를 다시 실행
                    calc(formula, '/', i)
                    i = 0
                else:
                    i += 1                              # i 번째 입력값이 숫자일 경우 i 값에 1을 더해 다음 입력값 검사
            else:                                       # 덧셈, 뺄셈 계산
                if formula[i] == '+':                   # i 번째 입력값이 덧셈일 경우 calc 함수를 실행하고 i 값을 초기화, 루프를 다시 실행
                    calc(formula, '+', i)
                    i = 0
                elif formula[i] == '-':                 # i 번째 입력값이 뺄셈일 경우 calc 함수를 실행하고 i 값을 초기화, 루프를 다시 실행
                    calc(formula, '-', i)
                    i = 0
                else:
                    i += 1                              # i 번째 입력값이 숫자일 경우 i 값에 1을 더해 다음 입력값 검사

        self.entry.delete(0, END)
        if "." in str(formula[0]):
            if len(str(formula[0])) > 20:               # 결과값이 소수점일 때 최대 소수점 이하 17자리까지만 표현
                self.entry.insert(0, round(formula[0], 17))
                self.count = len(str(abs(round(float(self.entry.get()), 17))))
            else:
                self.entry.insert(0, formula[0])
        else:
            self.entry.insert(0, formula[0])
            self.count = len(str(abs(int(self.entry.get()))))

# 계산기 프레임
root = Tk()

root.title("Calculator")
root.geometry("400x550+500+100")
root.resizable(0, 0)

upper_frame = Frame(root, width=400, height=70)
upper_frame.pack(pady=40)

down_frame = Frame(root, width=400, height=100)
down_frame.pack(padx=10, pady=10)

Main(root)

root.mainloop()