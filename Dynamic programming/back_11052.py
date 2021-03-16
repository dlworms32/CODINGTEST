"""
    카드 구매하기
"""

N = int(input())

cost = [0] * 1001

p = list(map(int, input().split()))
for i in range(1, N + 1):
    cost[i] = p[i - 1]

dp = [0] * 1001

dp[1] = cost[1]
dp[2] = max(cost[1] * 2, cost[2])
dp[3] = max(cost[1] * 3, max(cost[1] + cost[2], cost[3]))

for i in range(3, N + 1):
    for j in range(1, i + 1):
        dp[i] = max(dp[i], dp[j] + dp[i-j], cost[i])

print(dp[N])