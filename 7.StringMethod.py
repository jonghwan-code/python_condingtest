msg = "It is Time"
print(msg.upper())
print(msg.lower())
print(msg)

temp = msg.upper()
print(temp)
print(temp.find('T'))
print(temp.count('T'))
print(msg[:2])  # js slice 개념
print(msg[2:5])
print(len(msg))  # 문자열 길이

for i in range(len(msg)):
    print(msg[i], end=' ')
print()

# 문자열을 순회하며 반복한다. 여기에서 x는 인덱스 번호가 아니다
for x in msg:
    print(x, end=' ')
print()

for x in msg:
    if x.isupper():
        print(x, end=' ')
print()

for x in msg:
    if x.isalpha():
        print(x, end=' ')
print()

# 아스키 넘버 확인 함수
tmp = 'AZ'
for x in tmp:
    print(ord(x))

# 아스키 넘버로 문자열함수
num = 65

print(chr(num))
