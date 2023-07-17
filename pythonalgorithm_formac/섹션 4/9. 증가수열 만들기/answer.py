import sys
from collections import deque


def solution(input_file):
    sys.stdin = open(input_file, 'rt')
    n = int(input())
    a = list(map(int, input().split()))
    # a = deque(a)
    # tmp = []
    # direction = ''
    # last = 0

    # while a:
    #     left = a[0]
    #     right = a[-1]
    #     # 두 수 모두 last보다 클때
    #     if left > last and right > last:
    #         if left < right:
    #             x = a.popleft()
    #             tmp.append(x)
    #             last = tmp[-1]
    #             direction += 'L'
    #         else:
    #             x = a.pop()
    #             tmp.append(x)
    #             last = tmp[-1]
    #             direction += 'R'
    #     # 왼 수만 last 보다 클때
    #     elif left > last and right < last:
    #         x = a.popleft()
    #         tmp.append(x)
    #         last = tmp[-1]
    #         direction += 'L'
    #     # 오른 수만 last 보다 클때
    #     elif right > last and left < last:
    #         x = a.pop()
    #         tmp.append(x)
    #         last = tmp[-1]
    #         direction += 'R'
    #     # 둘다 last 보다 작을때
    #     else:
    #         # print(left, right, last)
    #         break
    # print(direction)
    # print(len(tmp))

    '''선생님 코드'''
    lt = 0
    rt = n-1
    tmp = []
    direction = ''
    last = 0

    while lt <= rt:
        if a[lt] > last:
            tmp.append((a[lt], 'L'))
        if a[rt] > last:
            tmp.append((a[rt], 'R'))
        tmp.sort()
        if len(tmp) == 0:
            break
        else:
            direction += tmp[0][1]
            last = tmp[0][0]
            if tmp[0][1] == 'L':
                lt += 1
            else:
                rt -= 1
        tmp.clear()


solution('in1.txt')
