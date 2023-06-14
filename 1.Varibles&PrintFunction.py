a = 1
A = 2
c1 = 3
# 2B = 4
print(a, A, c1)

# 선언된 변수에 새 값을 할당할 경우 새 값으로 값이 업데이트 된다.
# 여러 변수를 한번에 선언 가능
a, b, c = 4, 5, 6
print(a, b, c)

# 값 교환
a, b = 10, 20
print(a, b)
a, b = b, a
print(a, b)

# 변수 타입
a = 12345
print(type(a))
a = 12.3451233131313
print(type(a))
a = 'helloWorld'
print(type(a))


# 출력 방식
print("number")
a, b, c = 1, 2, 3
print(a, b, c)
print("number :", a, b, c)

print(a, b, c, sep=", ")
print(a, b, c, sep="\n")
print(a)
print(b)
print(c)
print(a, end=' ')
print(b, end=' ')
print(c)
