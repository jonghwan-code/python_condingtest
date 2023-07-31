import sys


def solution(input_file):
    sys.stdin = open(input_file, 'rt')
    res = []
    for i in range(2):
        word = input()
        p = dict()
        for x in word:
            # p 딕셔너리 안에서 키값이 있는지 없는지 확인하는 get 매소드(x 뒤 0은 값이 없으면 0으로 하라느 쯧)
            p[x] = p.get(x, 0) + 1
        res.append(p)

    for key in res[0].items():
        if key not in res[1]:
            print('NO')
            break
        else:
            if res[0][key] != res[1][key]:
                print('NO')
                break
    else:
        print("YES")
