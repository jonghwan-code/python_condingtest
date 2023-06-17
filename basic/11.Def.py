# 함수 정의 (print)
def add(a, b):
    c = a + b
    print(c)


add(5, 3)


# 함수 정의 (return, return 시 여러 개의 값을 리턴할 수 있다. 이때 반환은 튜플 형태로 한다.)
def cal(a, b):
    c = a + b
    d = a - b
    return c, d


print(cal(5, 3))


# practice1: 소수만 출력하는 함수

def isPrime(x):
    for i in range(2, x):
        if (x % i == 0):
            return False
    return True


li = [1, 2, 3, 4, 5]
for y in li:
    if isPrime(y):
        print(y, end=' ')
