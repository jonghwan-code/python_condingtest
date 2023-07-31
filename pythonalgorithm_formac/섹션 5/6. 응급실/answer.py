import sys
from collections import deque


def solution(input_file):
    sys.stdin = open(input_file, 'rt')

    '''내가 푼 코드'''
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = deque([(index, value) for index, value in enumerate(a)])
    res = [(-1, 0)]

    while res[-1][0] != k:
        x = a.popleft()
        for i in range(len(a)):
            if x[1] < a[i][1]:
                a.append(x)
                break
        else:
            res.append(x)
    return (len(res) - 1)

    '''선생님 코드
    cnt = 0
    while True:
        x = a.popleft()
        if any(x[1] < k[1] for k in a):
            a.append(x)
        else:
            cnt += 1
            if x[0] == k:
                break

    print(cnt)
    '''
