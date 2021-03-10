"""
    설탕 배달
"""

N = int(input())

box = 0

while True:
    if (N % 5) == 0:
        print(N // 5 + box)
        break

    N = N - 3
    box += 1

    if N < 0:
        print(-1)
        break