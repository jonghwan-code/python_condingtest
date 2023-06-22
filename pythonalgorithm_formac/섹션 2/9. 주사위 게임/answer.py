import sys


def solution(input_file):
    sys.stdin = open(input_file, 'rt')
    max = -2147000000
    n = int(input())
    max = 0
    for i in range(n):
        a = list(map(int, input().split()))
        a.sort()
        x, y, z = a
        # 3개 수 모두 같은 경우
        if x == y and y == z:
            a = 10000 + x * 1000
        # 2개 수 같은 경우 1
        elif x == y or x == z:
            a = 1000 + x * 100
        # 2개 수 같은 경우 2
        elif y == z:
            a = 1000 + y * 100
        # 3개 수 모두 다를 경우
        else:
            a = z * 100

        if a > max:
            max = a

    return max
