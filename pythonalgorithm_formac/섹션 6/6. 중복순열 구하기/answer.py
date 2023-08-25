import sys

sys.stdin = open('in1.txt', 'r')

# 중복순열: 중복이 가능하며 순서에 의미가 있는 순열
# 단순히 뽑는 원소만큼 for 문을 돌면 되지 않을까 싶지만, 만약 4개의 원소를 뽑을 경우 4번 for 문을 돌아야 한다.
def DFS(L):
    global count
    if L == m:
      for i in range(m):
        print(arr[i], end=' ')
      count += 1
      print()
    
    else:
      for i in range(1, n + 1):
          # [1, 0] 재귀 > [1, 1], [1, 2], [1, 3]
          # [2, 0] 재귀 > [2, 1], [2, 2], [2, 3]
          # [3, 0] 재귀 > [3, 1], [3, 2], [3, 3]
          arr[L] = i
          DFS(L + 1)

if __name__ == '__main__':
    n, m = map(int, input().split())
    count = 0
    result = []
    arr = [0] * m
    DFS(0)
    print(count)