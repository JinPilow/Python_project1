def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b
'''
def deleteright(s,a,b): #지울 리스트, 지울 숫자
    s=['3','+','2','+','1','+','2','*','3']
    formul1=''.join(formul)
    formul1.replace()
    print(formul1)
def deleteleft
'''

def replaceRight(original, old, new, count_right):
    repeat = 0
    text = original
    old_len = len(old)

    count_find = original.count(old)
    if count_right > count_find:  # 바꿀 횟수가 문자열에 포함된 old보다 많다면
        repeat = count_find  # 문자열에 포함된 old의 모든 개수(count_find)만큼 교체한다
    else:
        repeat = count_right  # 아니라면 입력받은 개수(count)만큼 교체한다

    while (repeat):
        find_index = text.rfind(old)  # 오른쪽부터 index를 찾기위해 rfind 사용
        text = text[:find_index] + new + text[find_index + old_len:]

        repeat -= 1

    return text


text = '123,456,789,999'
# text.replace(",", "", -1); print(text) #안됨

# text = replaceRight(text, ",", "", 2)
print("결과 :")
print(replaceRight(text, ",", "", 0))
print(replaceRight(text, ",", "", 1))
print(replaceRight(text, ",", "", 2))
print(replaceRight(text, ",", "", 3))
print(replaceRight(text, ",", "", 4))
'''
결과 :
123,456,789,999
123,456,789999
123,456789999
123456789999
123456789999
'''