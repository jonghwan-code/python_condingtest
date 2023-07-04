import sys


def reverseCheck(li):
    for i in range(2):
        left = i
        right = 5 - 1 - i
        if li[left] != li[right]:
            return False
            print()
            break
    else:
        return True


def solution(input_file):
    sys.stdin = open(input_file, 'rt')
    li = [list(map(int, input().split())) for _ in range(7)]
    res = 0
    for i in range(7):
        for j in range(3):
            checkRow = []
            checkCol = []
            for k in range(5):
                checkRow.append(li[i][j+k])
                checkCol.append(li[j+k][i])
            if reverseCheck(checkRow):
                res += 1
            if reverseCheck(checkCol):
                res += 1

    '''선생님 코드
    for i in range(3):
        for j in range(7):
            # 열은 slice 기능을 사용해서 5칸씩 자를 수 있다
            tmp = li[j][i:i+5]
            # 배열의 reverse [::-1]
            if tmp == tmp[::-1]:
                cnt += 1

            for k in range(2):
                if li[i+k][j] != li[i+5-1-k][j]:
                    break
            else:
                cnt += 1
    '''
    return res


solution('in1.txt')
