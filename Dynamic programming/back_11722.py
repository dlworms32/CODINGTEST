"""
    가장 긴 감소하는 부분 수열
"""
import sys

N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))

dp = [1] * N

for i in range(1, N):
    for j in range(i):
        if A[i] < A[j]:
            # 현재 i 위치의 값보다 큰 값의 개수를 구함
            dp[i] = max(dp[i], dp[j] + 1)

print(dp[N - 1])