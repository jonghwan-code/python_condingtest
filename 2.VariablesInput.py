'''
변수 입력과 연산자
'''


a = input("숫자를 입력하세요 : ")
print(a)

a, b = input("type a number each: ").split()
print(a, b)

# input에 입력된 값은 "문자열"이다
a, b = input("type a number for string : ").split()
print(a+b)


a, b = input("type a number for int : ").split()
a = int(a)
b = int(b)
print(a+b)

# map을 활용하여 input 창으로 전달 받은 숫자를 int type으로 일괄 변경
a, b = map(int, input("type a number with map : ").split())
print(a+b)

# 두 수의 타입이 다를 경우?
a = 4.5
b = 3
c = a + b
print(type(c))


# hello world
