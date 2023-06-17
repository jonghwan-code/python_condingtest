
x = 7

# 관계 연산자 == / !=
if x == 7:
    print('Lucky')
    print("Man")
# 중첩 if

x = 15

if x >= 10:
    if x % 2 == 1:
        print("10 이상의 홀수")
x = 9

if x > 0:
    if x < 10:
        print("10 보다 작은 자연수")


# 조건문에 and를 넣어 중첩 if 문과 같은 분기 처리 가능하다
x = 7
if x > 0 and x < 10:
    print("10 보다 작은 자연수")

# 부등호로 중첩 if 문과 같은 분기 처리 가능하다
x = 7
if 0 < x < 10:
    print("10 보다 작은 자연수")

# if else 분기문

x = 10

if x > 0:
    print("양수")
else:
    print("음수")


# 다중 if 문

x = 80

if x >= 90:
    print("A")
elif x >= 80:
    print("B")
elif x >= 70:
    print("C")
elif x >= 60:
    print("D")
else:
    print("F")
