"""
    블랙잭
"""

import sys

N, M = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))

answer = 0
d = M + 1
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            s = arr[i] + arr[j] + arr[k]
            if s == M:
                print(s)
                exit()
            else:
                if 0 < M - s < d:
                    answer = s
                    d = M - s
print(answer)