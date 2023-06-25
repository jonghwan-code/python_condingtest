import sys


def solution(input_file):
    sys.stdin = open(input_file, 'rt')
    n = int(input())
    a = list(map(int, input().split()))

    sum = 0
    acc = 0

    for i in a:
        if (i == 1):
            acc += 1
            sum += acc
        else:
            acc = 0

    return sum
