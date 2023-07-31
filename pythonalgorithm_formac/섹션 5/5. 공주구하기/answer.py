import sys
from collections import deque


def solution(input_file):
    sys.stdin = open(input_file, 'rt')
    k, n = map(int, input().split())
    a = list(range(1, k+1))
    a = deque(a)
    while len(a) != 1:
        count = 0
        while count != n:
            q = a.popleft()
            a.append(q)
            count += 1
        a.pop()
    return a[0]
