import sys


def solution(input_file):
    sys.stdin = open(input_file, 'rt')
    
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)

    def dfs(L, sum):
        if sum > total // 2:
          return
        if L == n:
            if sum == (total - sum):
                print('YES')
                sys.exit(0)
        else:
            dfs(L+1, sum + a[L])
            dfs(L+1, sum)    

    dfs(0,0)
    print('NO')
