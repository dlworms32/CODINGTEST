"""
    큐2
"""

from collections import deque
import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline())

    queue = deque()

    for _ in range(N):
        string = sys.stdin.readline()
        string_arr = string.split()

        if string_arr[0] == 'push':
            queue.append(int(string_arr[1]))

        elif string_arr[0] == 'pop':
            if len(queue) == 0:
                print(-1)
            else:
                print(queue.popleft())

        elif string_arr[0] == 'size':
            print(len(queue))

        elif string_arr[0] == 'empty':
            if len(queue) == 0:
                print(1)
            else:
                print(0)

        elif string_arr[0] == 'front':
            if len(queue) == 0:
                print(-1)
            else:
                print(queue[0])

        else: # back
            if len(queue) == 0:
                print(-1)
            else:
                print(queue[-1])