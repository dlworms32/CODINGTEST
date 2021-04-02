"""
    덩치
"""
import sys
N = int(sys.stdin.readline())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

rank_list = [0] * N
for i in range(len(arr)):  # 기준
    rank = 1
    for j in range(len(arr)):
        if i == j:
            continue
        s_weight, s_height = arr[i]
        c_weight, c_height = arr[j]

        if s_height < c_height and s_weight < c_weight:
            rank += 1

    rank_list[i] = rank

for i in rank_list:
    print(i, end=' ')
