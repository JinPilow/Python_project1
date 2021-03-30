from tkinter import *
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

def b_click(n):
    current = entry.get()
    entry.delete(0,END)
    entry.insert(0, str(current) + str(n))

def b_clear():
    pass


#버튼 0~9 설정
bnum =[]
for number in range(10):
    button1 = Button(down_frame, text=str(number), font=("Courier",18), padx = 15, pady = 10, command = lambda number=number: b_click(number))
    bnum.append(button1)

countnum=1
for row in range(3):
    for column in range(3):
        bnum[countnum].grid(row = 2-row,column = column, padx = 5, pady = 5)
        countnum += 1

bnum[0].grid(row = 3, column = 1, padx = 5, pady = 5)

#부호 설정
bsign = []
for sign in ["C","*","/","+","-","="]:
    button2 = Button(down_frame, text= sign, font=("Courier",18), padx = 15, pady = 10, command = lambda sign=sign: b_click(sign))
    bsign.append(button2)

countsign = 1
for row in range(5):
    bsign[countsign].grid(row = row,column = 3, padx = 5, pady = 5)
    countsign += 1

bsign[0].grid(row = 4, column = 2, padx = 5, pady = 5)



root.mainloop()



'''
formula = []

while True:
    term = input("계산식을 입력하시오") # 값을 입력받아 term에 임시 저장
    if term == "=": # term에 '='이 입력되면 입력 종료
        break
    formula.append(term) # 입력된 값을 formula 리스트에 저장
    if not formula[0].isnumeric(): # 예외처리1) 첫 입력값 숫자가 아닐 경우 종료
        print("잘못된 식입니다.")
        quit()
    for num in range(1, len(formula)): # 예외처리2) 연속되는 입력값의 자료형이 같은 경우 종료
        if formula[num].isdecimal() == formula[num-1].isdecimal():
            print("잘못된 식입니다.")
            quit()
    for number in formula[1::2]: # 예외처리3) 지정되지 않은 부호 입력시 종료
        if number not in ["*", "/", "+", "-"]:
            print("잘못된 식입니다.")
            quit()


from lib.Math import *

i = 0
while len(formula) > 1:
    if '*' in formula or '/' in formula: # 곱셈, 나눗셈 우선 계산
        if formula[i] == '*': # i 번째 입력값이 곱셈일 경우 calc 함수를 실행하고 i 값을 초기화, 루프를 다시 실행
            calc(formula, '*', i)
            i = 0
        elif formula[i] == '/': # i 번째 입력값이 나눗셈일 경우 calc 함수를 실행하고 i 값을 초기화, 루프를 다시 실행
            calc(formula, '/', i)
            i = 0
        else:
            i += 1 # i 번째 입력값이 숫자일 경우 i 값에 1을 더해 다음 입력값 검사
    else:  # 덧셈, 뺄셈 계산
        if formula[i] == '+': # i 번째 입력값이 덧셈일 경우 calc 함수를 실행하고 i 값을 초기화, 루프를 다시 실행
            calc(formula, '+', i)
            i = 0
        elif formula[i] == '-': # i 번째 입력값이 뺄셈일 경우 calc 함수를 실행하고 i 값을 초기화, 루프를 다시 실행
            calc(formula, '-', i)
            i = 0
        else:
            i += 1 # i 번째 입력값이 숫자일 경우 i 값에 1을 더해 다음 입력값 검사
print("Result: {}".format(formula))
'''