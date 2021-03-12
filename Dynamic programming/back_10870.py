"""
    피보나치 수 5
"""

n = int(input())

dp = [0] * (n + 1)

if n < 2:
    if n == 0:
        print(0)
    else:
        print(1)
else:
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 2] + dp[i - 1]

    print(dp[n])