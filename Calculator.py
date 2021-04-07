from tkinter import *
from tkinter import messagebox
from lib.Math import *
from decimal import Decimal

root = Tk()

root.title("Calculator")
root.geometry("400x550+500+100")
root.resizable(0, 0)

upper_frame = Frame(root, width=400, height=70)
upper_frame.pack(pady=40)

down_frame = Frame(root, width=400, height=100)
down_frame.pack(padx=10, pady=10)

entry = Entry(upper_frame, width=20, font=("Courier",18), borderwidth=5)
entry.pack()
entry.insert(0,"")



class Function:
    def __init__(self):
        self.count = 0
        Function.current = entry.get()

    def b_click(self, n):
        Function.current = entry.get()
        entry.delete(0,END)
        entry.insert(0, str(Function.current) + str(n))

        if not str(n).isdigit():
            self.count = 0
        elif str(n) == "00":
            self.count += 2
        else:
            self.count += 1
            print(self.count)

    def b_clear(self):
        Function.current = entry.get()
        temp = list(Function.current)
        del temp[-1]
        Function.current = ''.join(temp)
        entry.delete(0, END)
        entry.insert(0, Function.current)
        self.count = 0


    def b_allclear(self):
        entry.delete(0,END)
        self.count = 0

    def switch_sign(self):
        Function.current = entry.get()
        temp = Function.current[-self.count-1:]
        if not temp[0].isdigit():
            if len(temp) == 1:
                messagebox.showinfo("Error", "기능을 수행할 수 없습니다.")
            elif float(temp) < 0:
                currentre = self.current.replace(self.current[-self.count-1:], "+" + self.current[-self.count:])
            elif float(temp) > 0:
                currentre = self.current.replace(self.current[-self.count-1:], "-" + self.current[-self.count:])
        else:
            if float(temp) < 0:
                currentre = self.current.replace(self.current[-self.count:], "+" + self.current[-self.count:])
            elif float(temp) > 0:
                currentre = self.current.replace(self.current[-self.count:], "-" + self.current[-self.count:])
            else:
                currentre = 0
        entry.delete(0, END)
        entry.insert(0, currentre)

#"-3+4"             Function.current
#["-3", "+", "4"]   Formula

    def equal(self):
        Function.current = entry.get()
        formula = []
        temp = ""
        i = 0

        if Function.current[0] == "-":
            formula.extend(["0", "-"])
            i = 1
        elif Function.current[0] == "+":
            formula.extend(["0", "+"])
            i = 1
        else:
            while True:
                if Function.current[i].isdigit() or Function.current[i] == ".":
                    temp += Function.current[i]
                    i += 1
                elif not Function.current[i].isdigit():
                    formula.append(temp)
                    formula.append(Function.current[i])
                    temp = ''
                    i += 1
                if i == len(Function.current) - 1:
                    temp += Function.current[i]
                    formula.append(temp)
                    break
        try:
            i = 0
            while len(formula) > 1:
                if '*' in formula or '/' in formula:  # 곱셈, 나눗셈 우선 계산
                    if formula[i] == '*':  # i 번째 입력값이 곱셈일 경우 calc 함수를 실행하고 i 값을 초기화, 루프를 다시 실행
                        calc(formula, '*', i)
                        i = 0
                    elif formula[i] == '/':  # i 번째 입력값이 나눗셈일 경우 calc 함수를 실행하고 i 값을 초기화, 루프를 다시 실행
                        calc(formula, '/', i)
                        i = 0
                    else:
                        i += 1  # i 번째 입력값이 숫자일 경우 i 값에 1을 더해 다음 입력값 검사
                else:  # 덧셈, 뺄셈 계산
                    if formula[i] == '+':  # i 번째 입력값이 덧셈일 경우 calc 함수를 실행하고 i 값을 초기화, 루프를 다시 실행
                        calc(formula, '+', i)
                        i = 0
                    elif formula[i] == '-':  # i 번째 입력값이 뺄셈일 경우 calc 함수를 실행하고 i 값을 초기화, 루프를 다시 실행
                        calc(formula, '-', i)
                        i = 0
                    else:
                        i += 1  # i 번째 입력값이 숫자일 경우 i 값에 1을 더해 다음 입력값 검사
            entry.delete(0, END)
            entry.insert(0, formula[0])
        except IndexError as e:
            print(e)



#-3*-2
#3+3*-2
#3-2 = 3+ -2    1.빼기 뒤에 다른 부호가 오면 '-'와 숫자를 하나로 묶음
#+3+4           2.더하기가 식 맨 앞에 있거나 다른 부호 앞에 오면 생략한다.

'''
def equal():
    term = entry.get()
    formula = []
    temp = ''
    i = 0
    if term[0] == "-":
        temp += "-"
        term = term[1:]
    elif term[0] == "+":
        term = term[1:]
    if not term[0].isdigit() or not term[-1].isdigit:
        messagebox.showinfo("Error", "시작문자는 숫자로 입력해주세요.")
    else:
        while True:
            if term[i].isdigit() or term[i] == ".":
                temp += term[i]
                i += 1
            elif not term[i].isdigit():
                formula.append(temp)
                formula.append(term[i])
                temp = ''
                i += 1
            if i == len(term)-1:
                temp += term[i]
                formula.append(temp)
                break
        print(formula)
        for num in range(len(formula)):
            if num == 0:
                pass
            elif formula[num].isdecimal() == formula[num-1].isdecimal():
                messagebox.showinfo("Error", "연산할 수 없습니다.")
                entry.delete(0, END)
                break
    try:
        i = 0
        while len(formula) > 1:
            if '*' in formula or '/' in formula:  # 곱셈, 나눗셈 우선 계산
                if formula[i] == '*':  # i 번째 입력값이 곱셈일 경우 calc 함수를 실행하고 i 값을 초기화, 루프를 다시 실행
                    calc(formula, '*', i)
                    i = 0
                elif formula[i] == '/':  # i 번째 입력값이 나눗셈일 경우 calc 함수를 실행하고 i 값을 초기화, 루프를 다시 실행
                    calc(formula, '/', i)
                    i = 0
                else:
                    i += 1  # i 번째 입력값이 숫자일 경우 i 값에 1을 더해 다음 입력값 검사
            else:  # 덧셈, 뺄셈 계산
                if formula[i] == '+':  # i 번째 입력값이 덧셈일 경우 calc 함수를 실행하고 i 값을 초기화, 루프를 다시 실행
                    calc(formula, '+', i)
                    i = 0
                elif formula[i] == '-':  # i 번째 입력값이 뺄셈일 경우 calc 함수를 실행하고 i 값을 초기화, 루프를 다시 실행
                    calc(formula, '-', i)
                    i = 0
                else:
                    i += 1  # i 번째 입력값이 숫자일 경우 i 값에 1을 더해 다음 입력값 검사
        entry.delete(0, END)
        entry.insert(0, formula[0])
    except IndexError as e:
        print(e)
'''
#숫자 버튼 설정
bnum = []
func = Function()

for number in range(10):
    button1 = Button(down_frame, text=str(number), font=("Courier",18), padx = 15, pady = 10,
                     command = lambda number=number: func.b_click(number))
    bnum.append(button1)
bnum.append(Button(down_frame, text="00", font=("Courier",18), padx = 9, pady = 10,
                   command = lambda: func.b_click('00')))
bnum.append(Button(down_frame, text=".", font=("Courier",18), padx = 15, pady = 10,
                   command = lambda: func.b_click('.')))

countnum = 1
for row in range(3):
    for column in range(3):
        bnum[countnum].grid(row = 2-row,column = column, padx = 5, pady = 5)
        countnum += 1

bnum[0].grid(row = 3, column = 1, padx = 5, pady = 5)
bnum[10].grid(row = 3, column = 0, padx = 5, pady = 5)
bnum[11].grid(row = 3, column = 2, padx = 5, pady = 5)

#부호 버튼 설정
bsign = []
for sign in ["*","/","+","-"]:
    button2 = Button(down_frame, text= sign, font=("Courier",18), padx = 15, pady = 10,
                     command = lambda sign=sign: func.b_click(sign))
    bsign.append(button2)

bsign.append(Button(down_frame, text= "=", font=("Courier",18), padx = 15, pady = 10,
                    command = lambda: func.equal()))
bsign.append(Button(down_frame, text= "C", font=("Courier",18), padx = 15, pady = 10,
                    command = lambda: func.b_clear()))
bsign.append(Button(down_frame, text= "AC", font=("Courier",18), padx = 8, pady = 10,
                    command = lambda: func.b_allclear()))
bsign.append(Button(down_frame, text= "+/-", font=("Courier",18), padx = 2, pady = 10,
                    command = lambda: func.switch_sign()))

countsign = 0
for row in range(5):
    bsign[countsign].grid(row = row,column = 3, padx = 5, pady = 5)
    countsign += 1

bsign[4].grid(row = 4, column = 3, padx = 5, pady = 5)
bsign[5].grid(row = 4, column = 2, padx = 5, pady = 5)
bsign[6].grid(row = 4, column = 1, padx = 5, pady = 5)
bsign[7].grid(row = 4, column = 0, padx = 5, pady = 5)

root.mainloop()

'''
formula = []

while True:
    term = input("계산식을 입력하시오")        #값을 입력받아 term에 임시 저장
    if term == "=":                         #term에 '='이 입력되면 입력 종료
        break
    formula.append(term)                    #입력된 값을 formula 리스트에 저장
    if not formula[0].isnumeric():          #예외처리1) 첫 입력값 숫자가 아닐 경우 종료
        print("잘못된 식입니다.")
        quit()
    for num in range(1, len(formula)):      #예외처리2) 연속되는 입력값의 자료형이 같은 경우 종료
        if formula[num].isdecimal() == formula[num-1].isdecimal():
            print("잘못된 식입니다.")
            quit()
    for number in formula[1::2]:            #예외처리3) 지정되지 않은 부호 입력시 종료
        if number not in ["*", "/", "+", "-"]:
            print("잘못된 식입니다.")
            quit()


from lib.Math import *

i = 0
while len(formula) > 1:
    if '*' in formula or '/' in formula:    #곱셈, 나눗셈 우선 계산
        if formula[i] == '*':               #i 번째 입력값이 곱셈일 경우 calc 함수를 실행하고 i 값을 초기화, 루프를 다시 실행
            calc(formula, '*', i)
            i = 0
        elif formula[i] == '/':             #i 번째 입력값이 나눗셈일 경우 calc 함수를 실행하고 i 값을 초기화, 루프를 다시 실행
            calc(formula, '/', i)
            i = 0
        else:
            i += 1                          #i 번째 입력값이 숫자일 경우 i 값에 1을 더해 다음 입력값 검사
    else:                                   #덧셈, 뺄셈 계산
        if formula[i] == '+':               #i 번째 입력값이 덧셈일 경우 calc 함수를 실행하고 i 값을 초기화, 루프를 다시 실행
            calc(formula, '+', i)
            i = 0
        elif formula[i] == '-':             #i 번째 입력값이 뺄셈일 경우 calc 함수를 실행하고 i 값을 초기화, 루프를 다시 실행
            calc(formula, '-', i)
            i = 0
        else:
            i += 1                          #i 번째 입력값이 숫자일 경우 i 값에 1을 더해 다음 입력값 검사
print("Result: {}".format(formula))
'''