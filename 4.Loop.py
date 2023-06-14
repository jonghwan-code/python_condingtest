
'''
a = range(10)
print(list(a))

for i in range(10):
    print(i)

# rage 감소시키기

for i in range(10, 0, -1):
    print(i)


i = 1

while i <= 10:
    print(i)
    i += 1



i = 10

while i >= 1:
    print(i)
    i -= i

# break
i = 1

while True:
    print(i)
    if (i == 10):
        break
    i += 1
'''

# continue

for i in range(1, 11):
    if (i % 2 == 0):
        continue
    print(i)

# for ... else
# for 문 안에서 특정 조건에 따라 break가 된 경우 else문이 실행되지 않는다
for i in range(1, 11):
    print(i)
    if i == 5:
        break
else:
    print(11)
