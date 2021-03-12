"""
    정수 삼각형
"""

n = int(input())

tri = []

for i in range(n):
    tri.append(list(map(int, input().split())))

dp = [[0 for _ in range(len(tri[i]))] for i in range(n)]


dp[0][0] = tri[0][0]
dp[1][0] = tri[1][0] + dp[0][0]
dp[1][1] = tri[1][1] + dp[0][0]

for i in range(2, n):
    for j in range(len(tri[i])):
        if j == 0:
            dp[i][j] = dp[i - 1][0] + tri[i][0]

        elif j == (len(tri[i]) - 1):
            dp[i][j] = dp[i - 1][j - 1] + tri[i][j]

        else:
            dp[i][j] = max(dp[i - 1][j - 1] + tri[i][j],
                           dp[i - 1][j] + tri[i][j])

print(max(dp[n -1]))