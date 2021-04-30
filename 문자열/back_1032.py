"""
    명령 프롬프트
"""

import copy

N = int(input())

comd = [list(input()) for _ in range(N)]

result = copy.deepcopy(comd[0])
for i in range(N):
    for j in range(len(comd[i])):
        if result[j] != comd[i][j]:
            result[j] = '?'
print(''.join(result))