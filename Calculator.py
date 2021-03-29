from lib.Math import *

print("1 : 한번에 입력\n2 : 하나씩 입력\n")
while 1:
    mode = input("모드 : ")

    # 한번에 입력 계산기
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

        print("답은 : {}" .format(number[0]))
        quit()


    # 하나씩 입력 계산기
    elif mode == '2':

        print("(=까지 입력)")

        str = []        # 자료 저장 리스트
        temp = ''       # 문자 임시저장소
        test = True     # 문자, 숫자 확인 스위치(참 = 숫자검사, 거짓 = 부호검사)
        while True:
            temp = input(" >")
            if temp == '=':     # = 가 나오기전까지 입력 받기
                break
            else:
                if test:
                    if temp.isdigit():      # 숫자 확인
                        str.append(temp)
                        test = False
                    else:
                        print("숫자를 입력하세요!")
                else:
                    if issign(temp):        # 부호 확인
                        str.append(temp)
                        test = True
                    else:
                        print("부호를 입력하세요!")

        count = 0
        while count < len(str):
            if str[count] == '*' or str[count] == '/':
                function2(str, count)    # 계산 함수
            else:
                count += 1

        count = 0
        while count < len(str):
            if str[count] == '+' or str[count] == '-':
                function2(str, count)    # 계산 함수
            else:
                count += 1

        print("답은 : {}".format(str[0]))
        quit()

    else:
        print("모드를 잘못 입력하였습니다!")