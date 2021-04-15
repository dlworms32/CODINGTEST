"""
    동전 0
"""
import sys

N, K = map(int, sys.stdin.readline().split())

cost = [int(sys.stdin.readline())for i in range(N)]

num = 0

for i in range(N-1, -1, -1):
    if K >= cost[i]:
        num += K // cost[i]
        K = K % cost[i]
    if K == 0:
        break

print(num)