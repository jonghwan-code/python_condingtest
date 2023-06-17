
import sys


def solution(input_file):
    sys.stdin = open(input_file, 'rt')
    N = int(input())
    result = []
    for i in range(N):
        n, s, e, k = map(int, input().split())
        a = list(map(int, input().split()))
        a = a[s-1:e]
        a.sort()
        result.append('#%d %d' % (i+1, a[k-1]))
    print(result)


solution('in1.txt')
