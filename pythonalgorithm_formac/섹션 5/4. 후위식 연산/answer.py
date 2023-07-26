import sys


def solution(input_file):
    sys.stdin = open(input_file, 'rt')
    a = input()
    stack = []
    math = ['*', '/', '+', '-']

    for x in a:
        if x in math:
            tmp = eval((stack[-2] + x + stack[-1]))
            stack.pop()
            stack.pop()
            stack.append(str(tmp))
        else:
            stack.append(x)

    return int(stack[0])
