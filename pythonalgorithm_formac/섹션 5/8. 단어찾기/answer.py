import sys


def solution(input_file):

    sys.stdin = open(input_file, 'rt')
    N = int(input())
    p = dict()

    for i in range(N):
        word = input()
        p[word] = 1

    for j in range(N-1):
        word = input()
        p[word] = 0

    for key, val in p.items():
        if val == 1:
            print(key)
            break


solution('in5.txt')
