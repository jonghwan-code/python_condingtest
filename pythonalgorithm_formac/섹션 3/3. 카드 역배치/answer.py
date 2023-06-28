import sys


def solution(input_file):
    sys.stdin = open(input_file, 'rt')
    a = list(map(int, range(21)))
    res = ''
    for _ in range(10):
        s, e = map(int, input().split())
        mid = ((e - s) + 1) // 2

        for i in range(mid):
            a[s + i], a[e - i] = a[e - i], a[s + i]

    a.pop(0)
    for x in a:
        res = res + str(x) + ' '
    return res


solution('in1.txt')
