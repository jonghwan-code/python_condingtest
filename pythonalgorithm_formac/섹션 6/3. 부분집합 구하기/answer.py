import sys

def solution(input_file):
    sys.stdin = open(input_file)
    n = int(input())
    check = [0] * (n + 1)

    def dfs(v):
      if (v == n + 1):
          for i in range(1, n + 1):
              if check[i] == 1:
                  print('정답', i, end=' ')
          print()  
      else:
          check[v] = 1
          dfs(v + 1)
          print(check)
          check[v] = 0
          dfs(v + 1)
          print(check)
    dfs(1)

solution('in1.txt')

