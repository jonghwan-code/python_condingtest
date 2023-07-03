import sys


def dulipcateCheck(li):
    res = set(li)
    if len(res) == 9:
        return True
    else:
        return False


def check(li):
    for i in range(9):
        checkCol = []
        checkRow = []
        for j in range(9):
            # 행의 값이 중복되지 않는지
            # 열의 값이 중복되지 않는지
            checkRow.append(li[i][j])
            checkCol.append(li[j][i])
        if dulipcateCheck(checkRow) != True or dulipcateCheck(checkCol) != True:
            return False

    for k in range(3):
        for q in range(3):
            checkRect = []
            for s in range(3):
                for y in range(3):
                    checkRect.append(li[k*3+s][q*3+y])
            if dulipcateCheck(checkRect) != True:
                return False
    return True


def solution(input_file):
    sys.stdin = open(input_file, 'rt')
    li = [list(map(int, input().split())) for _ in range(9)]
    if check(li):
        return "YES"
    else:
        return "NO"


solution('in1.txt')
