import sys
from collections import deque


def solution(input_file):
    sys.stdin = open(input_file, 'rt')

    manC = list(input())
    N = int(input())
    a = [list(input()) for _ in range(N)]
    res = []
    for x in a:
        tmp = []
        for q in x:
            if q in manC:
                if tmp and tmp[-1] == q:
                    continue
                else:
                    tmp.append(q)
            else:
                continue
        if tmp == manC:
            res.append('YES')
        else:
            res.append('NO')

    print(res)
    # '''선생님 코드'''
    # for i in range(N):
    #     plan = input()
    #     dq = deque(manC)
    #     for x in plan:
    #         if x in dq:
    #             if x != dq.popleft():
    #                 print("#%d NO" % (i+1))
    #                 break
    #     else:
    #         if len(dq) == 0:
    #             print("#%d YES" % (i+1))
    #         else:
    #             print("#%d NO" % (i+1))
