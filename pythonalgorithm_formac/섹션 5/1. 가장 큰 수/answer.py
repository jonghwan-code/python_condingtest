import sys


def solution(input_file):

    sys.stdin = open(input_file, 'rt')

    number, n = map(int, input().split())
    number = list(map(int, str(number)))
    stack = []

    for x in number:
        while stack and n > 0 and stack[-1] < x:
            stack.pop()
            n -= 1
        stack.append(x)

    if n != 0:
        res = stack[:-n]
        res = ''.join(map(str, res))
        return int(res)

    else:
        res = ''.join(map(str, stack))
        return int(res)
