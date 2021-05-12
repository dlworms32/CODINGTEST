"""
    하얀 칸
"""

board = [list(input().strip()) for _ in range(8)]

black = False
count = 0
for i in range(8):
    for j in range(8):
        if black:  # 검정칸
            black = False
        else:  # 흰칸
            if board[i][j] == 'F':
                count += 1
            black = True

    if black:
        black = False
    else:
        black = True

print(count)