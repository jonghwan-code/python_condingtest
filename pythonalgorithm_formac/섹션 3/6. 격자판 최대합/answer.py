import sys


def solution(input_file):
    sys.stdin = open(input_file, 'rt')

    n = int(input())
    a = []
    subA = []
    subB = []
    max = 0
    for _ in range(n):
        x = list(map(int, input().split()))
        a.append(x)

    for i in range(n):
        t = a[i][i]
        u = a[i][n-1-i]
        subA.append(t)
        subB.append(u)
        if i == n-1:
            a.append(subA)
            a.append(subB)
    for y in range(n+2):
        sumNums = sum(a[y])
        if max < sumNums:
            max = sumNums

    return max
