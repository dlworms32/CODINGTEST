"""
    AC
"""
import sys
from collections import deque

T = int(sys.stdin.readline())

for i in range(T):
    p = sys.stdin.readline().strip()

    list_com = [i for i in p]
    queue_com = deque(list_com)

    n = int(sys.stdin.readline())

    if n == 0:
        input()
        arr = []
    else:
        arr = sys.stdin.readline()[1:-2]
        arr = deque(list(map(int, arr.split(','))))

    cond = True

    flag = False  # 뒤집힌 경우 True, 정상의 경우 False
    R_count = 0
    while queue_com:
        command = queue_com.popleft()

        if command == 'R':
            flag = not flag

        if command == 'D':
            if len(arr) == 0:
                print('error')
                cond = False
                break
            else:
                if flag:
                    arr.pop()
                else:
                    arr.popleft()

    if cond:
        if flag:
            arr.reverse()

        print('[', end='')
        for index, s in enumerate(arr):
            if index == len(arr) - 1:
                print(s, end='')
            else:
                print(s, end=',')
        print(']')