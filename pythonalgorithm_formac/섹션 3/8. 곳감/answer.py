import sys


def solution(input_file):
    sys.stdin = open(input_file, 'rt')

    N = int(input())
    li = [list(map(int, input().split())) for _ in range(N)]

    M = int(input())
    b = [list(map(int, input().split())) for _ in range(M)]

    gam = 0
    for i in range(M):
        r, a, m = b[i]
        pivot = m % N
        if a == 0:
            # copied = li[r-1][pivot:N] + li[r-1][0:pivot]
            # li[r-1] = copied
            '''선생님 코드'''
            # pop(0)으로 맨 앞의 값 빼내고, 그 값을 맨 뒤에 append해준다 (이걸 pivot 회 반복한다)
            for _ in range(pivot):
                li[r-1].append(li[r-1].pop(0))

        if a == 1:
            # copied = li[r-1][N-pivot:N] + li[r-1][0:N-pivot]
            # li[r-1] = copied
            '''선생님 코드'''
            # pop()으로 맨 뒤의 값 빼내고, 그 값을 맨 앞에 insert한다.
            for _ in range(pivot):
                li[r-1].insert(0, li[r-1].pop())
    s = 0
    e = N
    m = N // 2
    for i in range(N):
        for j in range(s, e):
            gam += li[i][j]
        if i < m:
            s += 1
            e -= 1
        else:
            s -= 1
            e += 1

    return gam
