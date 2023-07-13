import sys


def solution(input_file):
    sys.stdin = open(input_file, 'rt')

    def volumeCheck(capa):
        count = 1
        sum = 0
        for x in a:
            if sum + x > capa:
                count += 1
                sum = x

            else:
                sum += x
        return count

    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    lt = max(a)
    rt = sum(a)
    res = 0

    while lt <= rt:
        mid = (lt + rt) // 2
        tmp = volumeCheck(mid)
        if tmp <= m:
            res = mid
            rt = mid - 1
        else:
            lt = mid + 1

    print(res)


solution('in1.txt')
