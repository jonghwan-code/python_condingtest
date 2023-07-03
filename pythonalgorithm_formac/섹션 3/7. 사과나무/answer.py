import sys


def solution(input_file):
    sys.stdin = open(input_file, 'rt')
    N = int(input())
    a = [list(map(int, input().split())) for _ in range(N)]

    mid = N // 2
    s = e = mid
    apple = 0

    # 기준(mid)을 정하고 s,e 범위를 기준에 맞게 조정하며 반복문을 돈다
    for i in range(N):
        for j in range(s, e+1):
            apple += a[i][j]
        if i < mid:
            s -= 1
            e += 1
        else:
            s += 1
            e -= 1

    return apple


solution('in1.txt')
