import sys


def solution(input_file):

    sys.stdin = open(input_file, 'rt')

    n = int(input())
    stock = list(map(int, input().split()))
    c = int(input())
    # q = 0
    # w = 0
    # while c != 0:
    #     c -= 1
    #     max = -1247000000
    #     min = 1247000000
    #     for i, v in enumerate(stock):
    #         if v > max:
    #             max = v
    #             q = i
    #         elif v < min:
    #             min = v
    #             w = i
    #     print(max, min, c)
    #     stock[q] = max - 1
    #     stock[w] = min + 1
    #     print('stock', stock)

    # # print(max - 1 - min + 1)

    '''선생님 코드'''
    # 무작정 하드코딩이 아니라 간단하게 푸는 방법이 중요하다
    stock.sort()

    for _ in range(c):
        stock[0] += 1
        stock[n-1] -= 1
        stock.sort()

    return stock[n-1] - stock[0]


solution('in2.txt')
