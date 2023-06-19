import sys
import itertools


def solution(input_file):
    sys.stdin = open(input_file, 'rt')
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    res = set()

    # 조합 - 3개의 수를 순서 상관없이 무작위로 뽑음(1,2,3 과 2,1,3이 같음)
    for i in range(n):
        for j in range(i+1, n):
            for m in range(j+1, n):
                res.add(a[i]+a[j]+a[m])

    res = list(res)
    res.sort(reverse=True)
    return res[k-1]
    # 모듈 - itertools.combinations(리스트, 뽑는 개수)
    # nCr = list(set(list(map(sum, list(itertools.combinations(a, 3))))))
    # nCr.sort(reverse=True)
    # return nCr[k-1]
