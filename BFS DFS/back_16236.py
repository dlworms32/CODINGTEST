"""
    아기 상어
    0: 빈 칸
    1, 2, 3, 4, 5, 6: 칸에 있는 물고기의 크기
    9: 아기 상어의 위치
"""
import sys
import time
from collections import deque

    #  상 좌 우  하
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]


N = int(sys.stdin.readline())

M = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

size = 2

def bfs(x, y):
    visited = [[False] * N for _ in range(N)]  # 방문 기록
    copyM = [[0] * N for _ in range(N)]  # step 기록
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    able_list = []
    min_x = 0
    min_y = 0
    while queue:
        cx, cy = queue.popleft()

        for d in range(4):
            nx = dx[d] + cx
            ny = dy[d] + cy

            if 0 <= nx < N and 0 <= ny < N and copyM[nx][ny] == 0:
                if not visited[nx][ny]:
                    if 0 < M[nx][ny] < size:  # 먹을 수 있는 물고기인 경우
                        # print('eat fish from ({}, {}), size = {}, step = {}'.format(nx, ny,
                        #                                                             M[nx][ny],copyM[cx][cy] + 1))
                        # return nx, ny, copyM[cx][cy] + 1
                        able_list.append([nx, ny, copyM[cx][cy] + 1])
                        copyM[nx][ny] = copyM[cx][cy] + 1
                        visited[nx][ny] = True
                        if min_x > nx:
                            min_x = nx
                        if min_y > ny:
                            min_y = ny
                    elif M[nx][ny] == 0:  # 빈칸
                        queue.append((nx, ny))
                        visited[nx][ny] = True
                        copyM[nx][ny] = copyM[cx][cy] + 1
                    elif M[nx][ny] == size:  # 크기가 같은 물고기인 경우
                        queue.append((nx, ny))
                        copyM[nx][ny] = copyM[cx][cy] + 1
                        visited[nx][ny] = True

    if len(able_list) > 0:
        able_list.sort(key=lambda x: (x[2], x[0], x[1]))  # 배열 순서대로 정렬
        # print('able_list', able_list)
        r_x, r_y, step = able_list[0]
        return r_x, r_y, step
    else:
        return -1, -1, -1

sx = 0
sy = 0

result = 0
count = 0
size_count = 0
for i in range(N):
    for j in range(N):
        if M[i][j] == 9:
            sx = i
            sy = j
M[sx][sy] = 0
flag = False

# print(sx, sy, count)
# print('current size = ', size)
# print('result = ', result)
# print('------------------------------------------')
# for i in M:
#     print(i)

while True:
    # condition check
    for i in range(N):
        for j in range(N):
            if 0 < M[i][j] < size:
                flag = True

    if not flag:
        break

    sx, sy, count = bfs(sx, sy)
    M[sx][sy] = 0
    # print(sx, sy, count)
    # print('current size = ', size)
    # print('result = ', result)
    # print('------------------------------------------')
    # for i in M:
    #     print(i)
    if sx == -1 and sy == -1 and count == -1:
        break
    else:
        result += count
        size_count += 1
        if size_count == size:
            size_count = 0
            size += 1
print(result)