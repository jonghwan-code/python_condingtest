import sys


def solution(input_file):
    sys.stdin = open(input_file, 'rt')
    n = int(input())
    res = []
    for i in range(n):
        text = input()
        text = text.lower()
        midLen = len(text) // 2

        for x in range(midLen):
            left = x
            right = len(text) - 1 - left
            if text[left] == text[right]:
                continue
            else:
                # print('#%d NO' % (i+1))
                res.append('#%d NO\n' % (i+1))
                break
        else:
            # print('#%d YES' % (i+1))
            res.append('#%d YES\n' % (i+1))

    return res


'''

복습


def solution2(input_file):
    sys.stdin = open(input_file, 'rt')
    n = int(input())
    res = []
    for i in range(n):
        text = input()
        text = text.lower()

        if text != text[::-1]:
            print('#%d NO' % (i+1))
        else:
            print('#%d YES' % (i+1))

    return res

'''
