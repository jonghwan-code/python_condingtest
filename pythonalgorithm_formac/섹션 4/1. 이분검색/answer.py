import sys


def solution(input_file):
    sys.stdin = open(input_file, 'rt')
    N, M = map(int, input().split())
    a = list(map(int, (input().split())))
    a.sort()
    lt = 0
    rt = N - 1

    while lt <= rt:
        pivot = (lt + rt) // 2

        if a[pivot] == M:
            print(pivot+1)
            break
        elif a[pivot] > M:
            rt = pivot - 1
        else:
            lt = pivot + 1


solution('in1.txt')
