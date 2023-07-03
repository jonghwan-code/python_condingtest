import sys


# def solution(input_file):
#     sys.stdin = open(input_file, 'rt')

#     n = int(input())
#     a = [list(map(int, input().split())) for _ in range(n)]
#     subA = []
#     subB = []
#     largeNum = -2147000000

#     for i in range(n):
#         t = a[i][i]
#         u = a[i][n-1-i]
#         subA.append(t)
#         subB.append(u)
#         subC = []
#         for j in range(n):
#             q = a[j][i]
#             subC.append(q)
#             if j == n - 1:
#                 a.append(subC)
#         if i == n-1:
#             a.append(subA)
#             a.append(subB)
#     for y in range(n*2+2):
#         sumNums = sum(a[y])
#         if largeNum < sumNums:
#             largeNum = sumNums

#     return largeNum

'''
복습
'''


def solution(input_file):
    sys.stdin = open(input_file, 'rt')
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    largeNum = -2147000000

    for i in range(n):
        sum1 = sum2 = 0
        for j in range(n):
            sum1 += a[i][j]
            sum2 += a[j][i]
        if sum1 > largeNum:
            largeNum = sum1
        if sum2 > largeNum:
            largeNum = sum2

    sum1 = sum2 = 0
    for i in range(n):
        sum1 += a[i][i]
        sum2 += a[i][n-1-i]
    if sum1 > largeNum:
        largeNum = sum1
    if sum2 > largeNum:
        largeNum = sum2

    return largeNum
