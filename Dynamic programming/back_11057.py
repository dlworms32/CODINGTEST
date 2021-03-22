"""
    오르막 수
"""

import sys

N = int(sys.stdin.readline())

dp = [[0] * 10 for _ in range(N + 1)]
dp[0] = [1 for i in range(10)]

# N = 2일 때, 1의 자리가 2인 경우, 맨 앞 수는 0, 1, 2이다.
# 자릿수     0   1   2   3   4   5   6   7   8   9
#    1      1   1   1   1   1   1   1   1   1   1
#    2      1   2   3   4   5   6   7   8   9   10
#    3      1   3   6   10  15  21  28  36  45  55
#    ...

for i in range(1, N + 1):
    for j in range(10):
        for k in range(j + 1):
            dp[i][j] += dp[i - 1][k]

print(dp[N][9] % 10007)