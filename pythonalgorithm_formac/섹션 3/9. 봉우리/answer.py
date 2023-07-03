import sys


def valueCheck(li):
    max = li[0]
    for i in range(1, 5):
        if li[i] >= max:
            return False
            break

    else:
        return True


def solution(input_file):
    sys.stdin = open(input_file, 'rt')
    N = int(input())
    li = [list(map(int, input().split())) for _ in range(N)]

    added = [0]*(N+2)
    li.insert(0, added)
    li.append(added)

    for i in range(1, N+1):
        li[i].insert(0, 0)
        li[i].append(0)

    res = 0

    # for i in range(1, N+1):
    #     for j in range(1, N+1):
    #         value = li[i][j]
    #         a = li[i-1][j]
    #         b = li[i][j-1]
    #         c = li[i+1][j]
    #         d = li[i][j+1]
    #         q = [value, a, b, c, d]

    #         if valueCheck(q):
    #             res += 1

    '''선생님 코드'''
    # 상하좌우를 계산할때 [i][j]에 1을 더하거나 빼는 방식으로 순회하면서 값을 비교할 수 있구나..!!
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for i in range(1, N+1):
        for j in range(1, N+1):
            if all(li[i][j] > li[i+dx[k]][j+dy[k]] for k in range(4)):
                res += 1

    return res
