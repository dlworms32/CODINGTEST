"""
    터렛
"""
import math

T = int(input())

for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    dx = abs(x1 - x2)
    dy = abs(y1 - y2)

    d = math.sqrt(dx ** 2 + dy ** 2)

    if d == 0 and r1 == r2:
        print(-1)

    elif abs(r1 - r2) < d < (r1 + r2):  # 교점 2개
        print(2)

    elif d == abs(r1 - r2) or d == r1 + r2:  # 교점 1개
        print(1)

    else:
        print(0)