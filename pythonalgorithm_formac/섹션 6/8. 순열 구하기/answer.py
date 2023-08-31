
import sys

sys.stdin = open('in3.txt', 'r')


def DFS(L):
    global count
    if L == m:
        for i in range(L):
            print(arr[i], end=' ')
        count += 1
        print()

    else:
        for i in range(1, n+1):
            if check[i] == 0:
                check[i] = 1
                arr[L] = i
                DFS(L + 1)
                check[i] = 0


if __name__ == '__main__':
    n, m = map(int, input().split())
    count = 0
    arr = [0] * m
    check = [0] * (n+1)
    DFS(0)
    print(count)
