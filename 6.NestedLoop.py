a = range(5)

print(a)


for i in range(5):
    # print(i, sep='', end=' ')
    for j in range(i + 1):
        print("*", end=' ')
    print()


for i in range(5):
    # print(i, sep='', end=' ')
    for j in range(5 - i):
        print("*", end=' ')
    print()
