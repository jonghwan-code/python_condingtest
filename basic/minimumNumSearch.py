
li = [5, 3, 7, 9, 2, 5, 2, 6]
min = li[0]
for i in range(1, len(li)):
    if min > li[i]:
        min = li[i]
print(min)
