"""
    이동하기
"""

N, M = map(int, input().split())

maze = []

dp = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    maze.append(list(map(int, input().split())))

dp[0][0] = maze[0][0]

for i in range(1, N):
    dp[i][0] = maze[i][0] + dp[i-1][0]

for i in range(1, M):
    dp[0][i] = maze[0][i] + dp[0][i - 1]

for i in range(1, N):
    for j in range(1, M):
        dp[i][j] = max(dp[i-1][j] + maze[i][j], dp[i][j-1] + maze[i][j])

print(dp[N - 1][M - 1])