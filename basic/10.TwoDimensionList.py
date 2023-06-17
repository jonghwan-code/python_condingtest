# 값이 0인 1차원 리스트 만들기
a = [0]*3
print(a)


# 2차원 리스트 만들기
b = [[0]*3 for _ in range(3)]
print(b)


# 2차원 리스트의 형식은 행, 열을 가진 표와 같은 형식이다

for x in b:
    print(x)

'''
[0, 0, 0]
[0, 0, 0]
[0, 0, 0]
'''

for x in b:
    for y in x:
        print(y, end=' ')
    print()

'''
0 0 0 
0 0 0 
0 0 0 
'''
