import sys


def solution(input_file):

    sys.stdin = open(input_file, 'rt')
    text = input()
    numL = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    num = ''
    for x in text:
        if x in numL:
            num = num + str(x)

    newNum = int(num)
    cnt = 0
    for i in range(1, newNum + 1):
        if newNum % i == 0:
            cnt += 1

    return [str(newNum)+'\n', str(cnt)]


# '1'.isdecimal() => true
# 문자열이라고 하더라도 해당 문자열이 숫자로 이뤄진 값인지 확인해 주는 method이다

# '01234' 문자열을 숫자로 바꾸는 방법?
# result = 0
# for문을 돌면서 result * 10 + 0, result * 10 + 1, result * 10 + 2, result * 10 + 3, result * 10 + 4 하면
# 1234가 된다
