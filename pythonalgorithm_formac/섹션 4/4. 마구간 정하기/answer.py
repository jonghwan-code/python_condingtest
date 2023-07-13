import sys


def solution(input_file):
    sys.stdin = open(input_file, 'rt')

    n, c = map(int, input().split())
    horseLine = []
    for _ in range(n):
        tmp = int(input())
        horseLine.append(tmp)
    horseLine.sort()

    def horseCount(away):
        count = 1
        line = horseLine[0]
        for i in range(1, n):
            if horseLine[i] - line >= away:
                count += 1
                line = horseLine[i]
        return count

    # 가장 짧은 구간은 1이고, 가장 먼 구간은 가장 끝에 위치한 구간일 것이므로,
    lt = 1
    rt = horseLine[n-1]

    res = 0

    while lt <= rt:
        mid = (lt + rt) // 2

        # 임의의 최소값(mid)으로 세울 수 있는 말의 마리 수를 구하는 함수를 통과시켜
        # 그 마리수가 c(세우려는 말의 마리)보다 작으면 최소값이 줄어야 하므로 rt를 그만큼 줄인다.

        if horseCount(mid) >= c:
            res = mid
            lt = mid + 1
        else:
            rt = mid - 1

    return res
