"""
    탈출
"""
import sys
from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

R, C = map(int, sys.stdin.readline().split())

M = [list(sys.stdin.readline().strip()) for _ in range(R)]
path = [[0] * C for _ in range(R)]

def water(x, y):
    count = 1
    M[x][y] = 1
    while True:
        flag = False
        for i in range(R):
            for j in range(C):
                if M[i][j] == '.':
                    flag = True
        if not flag:
            break
        for i in range(R):
            for j in range(C):
                if M[i][j] == count:
                    for d in range(4):
                        nx = dx[d] + i
                        ny = dy[d] + j

                        if 0 <= nx < R and 0 <= ny < C:
                            if M[nx][ny] == '.':
                                M[nx][ny] = count + 1
        count += 1

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    path[x][y] = 1

    while queue:
        cx, cy = queue.popleft()

        for d in range(4):
            nx = dx[d] + cx
            ny = dy[d] + cy

            if 0 <= nx < R and 0 <= ny < C:
                if M[nx][ny] != 'X':
                    if M[nx][ny] == 'D':
                        return path[cx][cy]
                    if M[nx][ny] > path[cx][cy] + 1 and path[nx][ny] == 0:
                        path[nx][ny] = path[cx][cy] + 1
                        queue.append((nx, ny))
    return 'KAKTUS'

Dpos_x, Dpos_y = 0, 0
Wpos_x, Wpos_y = 0, 0

wp = False
sp = False
for i in range(R):
    for j in range(C):
        if wp and sp:
            break
        if M[i][j] == 'S':
            Dpos_x = i
            Dpos_y = j
            M[i][j] = '.'
            sp = True
        if M[i][j] == '*':
            Wpos_x = i
            Wpos_y = j
            wp = True

water(Wpos_x, Wpos_y)

for i in M:
    print(*i)
# print(bfs(Dpos_x, Dpos_y))

