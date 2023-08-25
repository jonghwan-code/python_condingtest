import sys
sys.stdin = open('in2.txt', 'r')

def DFS(L, sum, tsum):
  global max
  
  # 부분집합의 합이 max보다 적은 경우 return
  # > 해당 부분 집합의 나머지 값의 합이 max보다 적은 경우도 return 
  if sum + (total - tsum) < max:
    return 

  # 최대 용량보다 크면 return
  if sum > C:
    return 
  
  if L == N:
    if sum > max:
      max = sum

  else:
    DFS(L+1, sum + a[L], tsum + a[L])
    DFS(L+1, sum, tsum + a[L])

if __name__ == '__main__':
  C, N = map(int, input().split())
  a = []
  max = -2147000000
  
  for i in range(N):
    a.append(int(input()))
  
  total = sum(a)

  DFS(0, 0, 0)
  print(max)