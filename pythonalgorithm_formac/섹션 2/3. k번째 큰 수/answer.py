import sys
import itertools


def solution(input_file):
    sys.stdin = open(input_file, 'rt')
    N, k = map(int, input().split())
    a = list(map(int, input().split()))

    # 조합 - 3개의 수를 무작위로 뽑음 itertools.combinations(리스트, )
    nCr = list(set(list(map(sum, list(itertools.combinations(a, 3))))))
    nCr.sort(reverse=True)
    return nCr[k-1]
