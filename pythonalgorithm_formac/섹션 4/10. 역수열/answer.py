import sys


def solution(input_file):
    sys.stdin = open(input_file, 'rt')
    n = int(input())
    a = list(map(int, input().split()))
    a.reverse()

    tmp = []

    for i in range(n):
        t = i + (n-(i * 2))
        tmp.insert(a[i], t)

    return tmp
