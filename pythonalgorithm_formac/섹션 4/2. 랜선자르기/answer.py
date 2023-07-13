import sys


def solution(input_file):
    sys.stdin = open(input_file, 'rt')

    K, M = map(int, input().split())
    a = []
    res = 0

    for _ in range(K):
        tmp = int(input())
        a.append(tmp)

    maxNumber = max(a)

    lt = 1
    rt = maxNumber
    while lt <= rt:
        mid = (lt + rt) // 2
        tmp = 0
        for x in a:
            tmp += (x // mid)
        if tmp >= M:
            res = mid
            lt = mid + 1
        else:
            rt = mid - 1

    print(res)


solution('in1.txt')
