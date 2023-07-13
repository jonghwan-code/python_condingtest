import sys


def solution(input_file):
    sys.stdin = open(input_file, 'rt')
    n = int(input())
    person = [list(map(int, input().split())) for _ in range(n)]
    person = sorted(person, key=lambda x: (x[1], x[0]), reverse=True)
    print(person)
    # count = 1

    # for i in range(n-1):
    #     for j in range(i+1, n):

    #         h1, w1 = person[i]
    #         h2, w2 = person[j]
    #         if h2 > h1:
    #             break
    #     else:
    #         count += 1

    # return count

    '''
    선생님 코드 (시간 복잡도 면에서 훨씬 효과적이다)
    '''
    count = 0
    maxHeight = 0
    for x in person:
        h, w = x
        if h > maxHeight:
            maxHeight = h
            count += 1

    return count


solution('in5.txt')
