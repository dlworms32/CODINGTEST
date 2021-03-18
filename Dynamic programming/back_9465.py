"""
    스티커
"""
import sys

T = int(sys.stdin.readline())


for i in range(T):
    n = int(sys.stdin.readline())
    table = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]
    dp = [[0] * n for _ in range(2)]

    dp[0][0] = table[0][0]
    dp[1][0] = table[1][0]

    dp[0][1] = table[0][1] + dp[1][0]
    dp[1][1] = table[1][1] + dp[0][0]

    for i in range(2, n):
        dp[0][i] = max(dp[1][i - 1] + table[0][i],
                       dp[0][i - 2] + table[0][i],
                       dp[1][i - 2] + table[0][i])

        dp[1][i] = max(dp[0][i - 1] + table[1][i],
                       dp[0][i - 2] + table[1][i],
                       dp[1][i - 2] + table[1][i])

    print(max(dp[1][n - 1], dp[0][n - 1]))