"""
    구간 합 구하기 5
    빠른 입력 받기  sys.stdin.readline()
"""
import sys

N, M = map(int, sys.stdin.readline().split())

table = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[0] * (N + 1) for _ in range(N + 1)]


for i in range(N):
    for j in range(N):
        dp[i + 1][j + 1] = dp[i][j + 1] + table[i][j] + dp[i + 1][j] - dp[i][j];

for i in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    print(dp[x2][y2] - dp[x2][y1 - 1] - dp[x1 - 1][y2] + dp[x1 - 1][y1 - 1])