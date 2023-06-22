import sys

'''내가 푼 코드'''


def reverse(num):
    num = str(num)
    a = [i for i in num]
    for left in range(len(a) // 2):
        right = len(a) - left - 1
        tmp = a[left]
        a[left] = a[right]
        a[right] = tmp
    res = ''
    for x in a:
        res += x
    return int(res)


def isPrime(n):
    if n < 2:
        return False
    for i in range(2, n // 2+1):
        if n % i == 0:
            return False

    return True


def solution(input_file):
    sys.stdin = open(input_file, 'rt')
    n = int(input())
    a = list(map(int, input().split()))
    res = ''
    for x in a:
        p = reverse(x)
        if isPrime(p):
            res += str(p) + ' '

    return res


'''복습


def reverse2(num):
    res = 0

    while num:
        t = num % 10  # num의 일의 자리를 구할 수 있다.
        num = num // 10  # num의 일의 자리를 뺀, 즉 10으로 나눈 몫을 알 수 있다.
        res = res * 10 + t
    return res

'''
