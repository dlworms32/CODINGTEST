"""
    N과 M (1)
"""
from itertools import permutations

N, M = map(int, input().split())

# 중복되지 않는 수열 만들기
P = permutations(range(1, N + 1), M)

for i in P:
    print(' '.join(map(str, i)))