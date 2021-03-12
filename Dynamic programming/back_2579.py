"""
    계단 오르기
"""

n = int(input())

step = [0] * n

for i in range(n):
    step[i] = int(input())

if n < 3:
    print(sum(step))

else:
    dp = [0] * n

    dp[0] = step[0]
    dp[1] = max(step[0] + step[1], step[1])
    dp[2] = max(step[0] + step[2], step[1] + step[2])

    for i in range(3, n + 1):
        if i >= n:
            break
        dp[i] = max(dp[i - 2] + step[i], dp[i - 3] + step[i - 1] + step[i])

    print(dp[n-1])