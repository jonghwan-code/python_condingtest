import sys


def solution(input_file):
    sys.stdin = open(input_file, 'rt')
    li = input()
    sum = 0
    stack = []
    for i in range(len(li)):
        if li[i] == '(':
            stack.append(li[i])
        else:
            stack.pop()
            if li[i - 1] == '(':
                sum += len(stack)
            else:
                sum += 1


solution('in1.txt')
