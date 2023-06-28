import sys


def solution(input_file):
    sys.stdin = open(input_file, 'rt')

    n = input()
    a = list(map(int, input().split()))
    m = input()
    b = list(map(int, input().split()))
    res = [0]*(len(a) + len(b))
    # 병합 정렬이다
    i1 = 0
    i2 = 0
    ip = 0

    while i1 < n and i2 < m:
        if a[i1] < b[i2]:
            res[ip] = a[i1]
            i1 += 1
            ip += 1
        else:
            res[ip] = b[i2]
            i2 += 1
            ip += 1

    while i1 < n:
        res[ip] = a[i1]
        i1 += 1
        ip += 1

    while i2 < m:
        res[ip] = b[i2]
        i2 += 1
        ip += 1

    return res
