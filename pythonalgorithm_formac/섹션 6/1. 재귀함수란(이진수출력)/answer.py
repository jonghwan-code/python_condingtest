import sys

def decimal2Binary(x):
  quotient = x // 2
  remainder = x % 2
  
  if x == 0:
    return
  else:
    decimal2Binary(quotient)
    print(remainder, end='')

def solution(input_file):
  sys.stdin = open(input_file, 'rt')
  number = int(input())
  decimal2Binary(number)

solution('in1.txt')