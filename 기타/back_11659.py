"""
    구간 합 구하기 4
"""
import sys

N, M = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))

sum_arr = [0] * N

sum_arr[0] = arr[0]

for i in range(1, N):
    sum_arr[i] = sum_arr[i - 1] + arr[i]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    i, j = i - 1, j - 1
    if i == 0:
        print(sum_arr[j])
    else:
        print(sum_arr[j] - sum_arr[i - 1])