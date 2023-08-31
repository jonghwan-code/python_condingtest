

import sys

sys.stdin = open('in5.txt', 'r')


def DFS(L, sum):
    global ch
    if L == n and sum == f:
        # print(p)
        for x in p:
            print(x, end=' ')
        sys.exit(0)
    else:
        for i in range(1, n+1):
            if ch[i] == 0:
                ch[i] = 1
                p[L] = i
                DFS(L + 1, sum + p[L] * b[L])
                ch[i] = 0


if __name__ == '__main__':
    n, f = map(int, input().split())
    # n의 값에 따른 combination 배열을 생성해 준다
    ch = [0] * (n + 1)
    p = [0] * n
    b = [1] * n
    for i in range(1, n):
        b[i] = b[i-1] * (n - i) // i
    DFS(0, 0)
