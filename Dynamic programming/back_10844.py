"""
    쉬운 계단 수
"""
import sys

dp = [[0] * 10 for _ in range(101)]

N = int(sys.stdin.readline())

dp[1] = [1 for _ in range(10)]
dp[1][0] = 0


for i in range(2, N + 1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i - 1][1]
        elif j == 9:
            dp[i][j] = dp[i - 1][8]
        else:
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1])

answer = 0

for i in dp[N]:
    answer += i

print(answer % 1000000000)
