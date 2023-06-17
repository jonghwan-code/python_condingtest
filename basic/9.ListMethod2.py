# 리스트 slice [:]
a = [23, 12, 36, 53, 19]
print(a[:3])
print(a[3:])
print(a[1:3])
print(len(a))

# for문으로 리스트 반복문 돌기

for i in range(0, len(a)):
    print(a[i], end=' ')
print()

# index로 안 돌아도 바로 값 접근 가능
for x in a:
    print(x, end=' ')
print()


# enumerate (튜플 형태로 변환)
for x in enumerate(a):
    print(x)

for index, value in enumerate(a):
    print(index, value)


# if all 함수 (js array.every())
if all(60 > x for x in a):
    print("ALL YES")
else:
    print("NO")

# if any 함수 (js의 array.some())
if any(15 > x for x in a):
    print("ANY YES")
else:
    print("NO")
