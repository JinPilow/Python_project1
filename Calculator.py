from lib.Math import *

mode = input("1 : 한번에 입력\n2 : 하나씩 입력\n모드 : ")

#한번에 입력
if mode == '1':

    str = input("입력 (=제외) >")

    sign = []  # 부호 리스트
    number = []  # 숫자 리스트
    temp = ""  # 십의자리 이상 저장용
    if str[0].isdigit():  # 숫자로 시작하는지 확인
        for i in range(len(str)):
            if str[i].isdigit():  # 숫자확인후 temp에 저장
                temp += str[i]
            elif issign(str[i]):  # 부호일 경우 temp를 number에 저장하고 부호는 sign에 저장
                number.append(temp)
                temp = ""
                sign.append(str[i])
            else:  # 그 의외의 문자면 경고 출력후 프로그램 종료
                print("숫자와 사칙연산만 입력해주세요!")
                quit()
            if i + 1 == len(str):  # 마지막 숫자 number에 저장
                number.append(temp)
    else:  # 예외처리
        print("숫자로 시작해 주세요!")
        quit()

    count = 0  # 인덱스 변수
    while count < len(sign):
        if sign[count] == '*' or sign[count] == '/':  # 곱하기, 나누기 계산
            number[count] = calculat(sign[count], float(number[count]), float(number[count + 1]))
            del number[count + 1]
            del sign[count]
        else:
            count += 1  # 연산을 안햇을시 다음 인덱스, 안햇을시 인덱스 유지(계산된건 삭제되기 때문)

    count = 0
    while count < len(sign):
        if sign[count] == '+' or sign[count] == '-':  # 더하기, 빼기 계산
            number[count] = calculat(sign[count], float(number[count]), float(number[count + 1]))
            del number[count + 1]
            del sign[count]
        else:
            count += 1

    print(eval(str))
    print(number)
    # print(str) 5+32-2*13/5

#하나씩 입력 계산기
elif mode == '2':

    print("(=까지 입력)")
    str = []
    temp = ''
    while True:
        temp = input(" >")
        if temp != '=':
            str.append(temp)
        else:
            break


    count = 0
    while count < len(str):
        if str[count] == '*' or str[count] == '/':
            str[count-1] = calculat(str[count], float(str[count-1]), float(str[count+1]))
            del str[count]
            del str[count]
        else:
            count += 1

    count = 0
    while count < len(str):
        if str[count] == '+' or str[count] == '-':
            str[count-1] = calculat(str[count], float(str[count-1]), float(str[count+1]))
            del str[count]
            del str[count]
        else:
            count += 1

    print(str)
# 3*2+2/2-1