import sys

sys.stdin = open('in4.txt', 'r')
# 원소를 한대로 선택할 수 있다.... for 문 제한도 없다.... 그러면.....

# 동전의 합을 구하면서 진행 > 합이 15보다 크면 return
# 동전의 수가 min보다 크면 return
# 합이 15인 경우, 동전의 수가 min 보다 작으면 min 갱신
# 이외는 for문 + 재귀 함수 조합으로 구현


def DFS(sum, count):
    global min

    if sum > m:
        return
    if count > min:
        return
    if sum == m:
        if count < min:
            min = count
    else:
        for x in a:
            DFS(sum + x, count + 1)


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    # print(a)
    m = int(input())
    min = 2147000000
    DFS(0, 0)
    print(min)
