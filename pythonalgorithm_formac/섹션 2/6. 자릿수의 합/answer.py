import sys


def solution(input_file):
    sys.stdin = open(input_file, 'rt')

    n = int(input())

    '''내가 푼 방식'''
    # a = list(map(str, input().split()))
    # res = [0]*len(a)
    # for i, v in enumerate(a):
    #     sum = 0
    #     for j in range(len(v)):
    #         sum += int(v[j])
    #         if j == len(v) - 1:
    #             res[i] = sum
    # max = 0
    # for k in range(len(a)):
    #     if res[k] > max:
    #         max = res[k]

    # return a[res.index(max)]

    '''복습'''
    a = list(map(int, input().split()))

    def digit_sum(num):
        sum = 0
        # for x in str(num):
        #     sum += int(x)
        # return sum

        while num > 0:
            sum += num % 10  # 일의 자리 값을 sum한다.
            num = num // 10  # 일의 자리를 값을 삭제한다.

        return sum

    max = -2147000000

    for i in a:
        tot = digit_sum(i)
        if tot > max:
            max = tot
            res = i
    return res


solution('in1.txt')
