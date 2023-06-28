import sys


def solution(input_file):
    sys.stdin = open(input_file, 'rt')

    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    lt = 0
    rt = 1
    tot = a[0]
    cnt = 0
    # while 문이 행해지는 동안 계속해서 tot값이 변경되어간다
    while True:
        if tot < m:
            if rt < n:
                tot += a[rt]
                rt += 1
            else:
                break
        elif tot == m:
            cnt += 1
            tot -= a[lt]
            lt += 1

        else:
            tot -= a[lt]
            lt += 1

    return cnt


solution('in1.txt')
