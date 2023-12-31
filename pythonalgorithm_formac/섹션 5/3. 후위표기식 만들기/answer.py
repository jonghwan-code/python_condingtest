import sys


def solution(input_file):
    sys.stdin = open(input_file, 'rt')

    a = input()
    res = ''
    stack = []

    # 연산 우선 순위?
    #
    print(a)
    for x in a:
        if x.isdecimal():
            res += x
        else:
            if x == '(':
                stack.append(x)
            elif x == '*' or x == '/':
                while stack and (stack[-1] == '*' or stack[-1] == '/'):
                    res += stack.pop()
                stack.append(x)
            elif x == '+' or x == '-':
                while stack and stack[-1] != '(':
                    res += stack.pop()
                stack.append(x)
            elif x == ')':
                while stack and stack[-1] != '(':
                    res += stack.pop()
                stack.pop()
    while stack:
        res += stack.pop()

    return res


solution('in1.txt')
