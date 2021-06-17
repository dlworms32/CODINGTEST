"""
    군형잡힌 세상
"""
import sys
from collections import deque

while True:
    string = sys.stdin.readline().strip('\n')

    if string == '.':
        break
    flag = False
    stack = deque()
    for char in string:
        if char == '[':
            stack.append('[')

        elif char == '(':
            stack.append('(')

        elif char == ']':
            if len(stack) > 0:
                if stack.pop() != '[':
                    flag = True
            else:
                flag = True

        elif char == ')':
            if len(stack) > 0:
                if stack.pop() != '(':
                    flag = True
            else:
                flag = True

    if flag or len(stack) > 0:
        print('no')
    else:
        print('yes')