"""
    체스판 다시 칠하기
"""
import sys
N, M = map(int, sys.stdin.readline().split())

board = [list(sys.stdin.readline().replace('\n', '')) for _ in range(N)]

diff_color = 64

for i in range(N - 7):
    for j in range(M - 7):
        num_repaint = 0

        for c in ['W', 'B']:
            color_next = c
            count = 0
            for x in range(i, i + 8):
                for y in range(j, j + 8):
                    if color_next != board[x][y]:
                        count += 1
                    if color_next == 'B':
                        color_next = 'W'
                    else:
                        color_next = 'B'

                if color_next == 'B':
                    color_next = 'W'
                else:
                    color_next = 'B'
            if count < diff_color:
                diff_color = count

print(diff_color)
