"""
    드래곤 커브
"""
import sys
import time

#     0, 1,  2, 3
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

N = int(sys.stdin.readline())

curves = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

M = [[False] * 101 for _ in range(101)]

# x, y: 시작 위치  d: 방향  g: 세대
def dragon_curve(x, y, d, g):
    curve = [d]
    M[x][y] = True  # 시작 위치

    for i in range(g):
        for index in range(len(curve) - 1, -1, -1):
            curve.append((curve[index] + 1) % 4)

    for direct in curve:
        x = dx[direct] + x
        y = dy[direct] + y
        M[x][y] = True

    # for i in range(10):
    #     for j in range(10):
    #         print(M[i][j], end=' ')
    #     print()
    # print('==========================')


for x, y, d, g in curves:
    # print(x, y, d, g)
    dragon_curve(y, x, d, g)

count = 0
for i in range(100):
    for j in range(100):
        if M[i][j]:
            if M[i + 1][j] and M[i][j + 1] and M[i + 1][j + 1]:
                count += 1

print(count)

