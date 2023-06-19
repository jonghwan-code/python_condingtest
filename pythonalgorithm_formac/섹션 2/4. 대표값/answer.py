import sys


def solution(input_file):
    sys.stdin = open(input_file, 'rt')
    n = int(input())
    a = list(map(int, input().split()))
    ave, y = str(sum(a) / len(a)).split('.')
    if int(y) >= 5:
        ave = int(ave) + 1
    else:
        ave = int(ave)

    min = float('inf')
    for idx, value in enumerate(a):
        tmp = abs(value - ave)
        if tmp < min:
            min = tmp
            score = value
            res = idx + 1
        elif tmp == min:
            if value > score:
                score = value
                res = idx + 1

    return str(ave) + ' ' + str(res)
