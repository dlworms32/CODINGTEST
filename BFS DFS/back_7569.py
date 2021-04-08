"""
    토마토
"""
import sys
from collections import deque

# 상, 하, 좌, 우, 윗층, 아래층
dx = [0, 0, 0, 0, -1, 1]
dy = [-1, 1, 0, 0, 0, 0]
dz = [0, 0, -1, 1, 0, 0]

M, N, H = map(int, sys.stdin.readline().split())

arr = []

for _ in range(H):
    temp = []
    for j in range(N):
        temp.append(list(map(int, sys.stdin.readline().split())))
    arr.append(temp)


def bfs(a, pos):
    global M, N, H
    queue = deque()
    for x, y, z in pos:
        queue.append((x, y, z))
    date = 0
    while queue:
        cx, cy, cz = queue.popleft()
        date = a[cx][cy][cz]

        for i in range(6):
            nx = dx[i] + cx
            ny = dy[i] + cy
            nz = dz[i] + cz

            if -1 < nx < H and -1 < ny < N and -1 < nz < M:
                if a[nx][ny][nz] == 0:
                    a[nx][ny][nz] = a[cx][cy][cz] + 1
                    queue.append((nx, ny, nz))

    for i in range(H):
        for j in range(N):
            for k in range(M):
                if a[i][j][k] == 0:
                    return -1

    return date - 1

arr_pos = []

for i in range(H):
    for j in range(N):
        for k in range(M):
            if arr[i][j][k] == 1:
                arr_pos.append((i, j, k))

print(bfs(arr, arr_pos))
