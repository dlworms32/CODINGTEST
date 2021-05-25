"""
    요세푸스 문제
"""
import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

l = [i for i in range(1, N + 1)]
queue = deque(l)

result = deque()
while queue:
    queue.rotate(-(K - 1))
    result.append(queue.popleft())

print('<', end='')
print(*list(result), sep=', ', end='')
print('>')