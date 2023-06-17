import random as r

a = []
b = list()
c = list(range(1, 10))
d = list(range(10, 16))

# 두 개 리스트 병합하기 +
e = c + d
print(e)


# 리스트에 값 추가하기 append, insert
e.append(16)
print((c + d).append(16))  # 이렇게 하면 none
print(e)

e.insert(10, 17)  # index 10에 17이라는 값 넣기
print(e)


# 리스트에서 값 제거하기 pop remove
e.pop()  # 리스트의 가장 마지막 index의 값 제거
print(e)

e.pop(10)  # 리스트의 index 0의 값 제거
print(e)

e.remove(14)  # remove는 리스트의 특정 값을 제거해 준다print(e)
print(e)


# 리스트의 특정 값 인덱스 확인하기
print(e.index(10))


# 리스트의 합 sum
a = list(range(1, 11))
print(sum(a))


# 리스트의 최대값 최소값
print(max(a))
print(min(a))
print(min(3, 100))


# [sort] : random, sort, reverse

r.shuffle(a)
print(a)

a.sort(reverse=True)  # 기본적으로 sort는 오름차순으로 하지만 reverse = True 조건을 걸어주면 내림차순으로 정렬한다
print(a)

a.sort()
print(a)
