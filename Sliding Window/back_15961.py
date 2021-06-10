"""
    회전 초밥
"""
import sys
from collections import deque, Counter

N, d, k, c = map(int, sys.stdin.readline().split())

table = [int(sys.stdin.readline()) for _ in range(N)]

sushi_dict = Counter(table[0:k])
queue = deque(table[0:k])

max_result = 0
length = len(sushi_dict)
if c in sushi_dict:
    max_result = max(length, max_result)
else:
    max_result = max(length + 1, max_result)

for i in range(N):
    pop_sushi = queue.popleft()
    sushi_dict[pop_sushi] -= 1
    if sushi_dict[pop_sushi] == 0:
        del sushi_dict[pop_sushi]
        length -= 1
    queue.append(table[(k + i) % N])
    if table[(k + i) % N] in sushi_dict:
        sushi_dict[table[(k + i) % N]] += 1
    else:
        sushi_dict[table[(k + i) % N]] = 1
        length += 1

    if c in sushi_dict:
        max_result = max(length, max_result)
    else:
        max_result = max(length + 1, max_result)

print(max_result)
