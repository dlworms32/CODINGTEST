"""
    1, 2, 3 더하기
"""

N = int(input())

for i in range(N):
    n = int(input())
    dp = [0] * 11
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for j in range(4, n + 1):
        dp[j] = dp[j - 3] + dp[j - 2] + dp[j - 1]

    print(dp[n])