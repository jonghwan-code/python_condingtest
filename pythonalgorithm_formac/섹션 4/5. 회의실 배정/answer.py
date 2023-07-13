import sys


def solution(input_file):
    sys.stdin = open(input_file, 'rt')
    n = int(input())
    meetings = [list(map(int, input().split())) for _ in range(n)]

    # 가장 빨리 끝나는 회의를 넣어 주고,
    # 해당 회의 이외의 회의 중에서 또 가장 빨리 마치되 먼저 진행한 회의와 겹치지 않는 회의를 스케쥴링하자
    schedules = 0

    # 미팅 마치는 시간을 오름차순으로 정렬하고나서, 미팅 마치는 시간이 같지만 시작 시간이 다른 회의를 시작 시간을 오름차순으로 정렬
    meetings = sorted(meetings, key=lambda x: (x[1], x[0]))

    # print(meetings)

    init_e = 0
    for x in meetings:
        s, e = x
        if s >= init_e:
            schedules += 1
            init_e = e
    return schedules


solution('in1.txt')
