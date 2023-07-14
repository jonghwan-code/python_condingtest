import sys
from collections import deque


def solution(input_file):
    sys.stdin = open(input_file, 'rt')
    n, m = map(int, input().split())
    people = list(map(int, input().split()))
    people.sort()
    # 배열에서 값을 제거하면 모든 요소가 인덱스 이동을 하지만, deque는 앞뒤의 값을 제거하더라도 인덱스 값이 유지된다
    people = deque(people)
    count = 0
    # while len(people) > 0:
    #     copied = people
    #     for i in range(n):
    #         big = copied[len(copied)-1]
    #         small = copied[i]
    #         if big + small > m:
    #             copied.pop()
    #             count += 1
    #             break
    #         else:
    #             copied.pop(0)
    #             copied.pop()
    #             count += 1
    #             break
    '''선새님 코드'''
    # 앞뒤에 최소/최대값이 존재하므로 굳이 for 문을 돌지 않아도 된다

    while people:
        if len(people) == 1:
            count += 1
            break
        if people[0] + people[-1] > m:
            people.pop()
            count += 1

        else:
            people.popleft
            people.pop()
            count += 1

    print(count)


solution('in2.txt')
