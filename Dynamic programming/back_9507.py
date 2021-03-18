
import sys

dp = [0] * 68
dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4, 68):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3] + dp[i - 4]

t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    print(dp[n])

