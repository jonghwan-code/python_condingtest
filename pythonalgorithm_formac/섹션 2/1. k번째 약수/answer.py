import sys


def solution(input_file):
    sys.stdin = open(input_file, 'rt')
    n, k = map(int, input().split())
    cnt = 0
    for i in range(1, n+1):
        if n % i == 0:
            cnt += 1
            if cnt == k:
                return i
                break
    else:
        return -1
