import sys

# 4, 6, 8, 12, 20

# 4 = [1,2,3,4]
# 6 = [1,2,3,4,5,6]


def solution(input_file):
    sys.stdin = open(input_file, 'rt')
    n, k = map(int, input().split())

    cnt = [0]*(n+k+1)
    max = 0
    result = ''
    for i in range(1, n+1):
        for j in range(1, k+1):
            cnt[i+j] += 1

    for m in range(n+k+1):
        if cnt[m] > max:
            max = cnt[m]

    for q in range(n+k+1):
        if cnt[q] == max:
            result = result + str(q) + ' '

    return result
