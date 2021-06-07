"""
    상근이의 여행
"""
import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())

    graph = [[] for _ in range(N + 1)]
    visited = [0] * (N + 1)
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    queue = deque()
    queue.append(1)
    visited[1] = 1

    count = 0
    while queue:
        x = queue.popleft()

        for node in graph[x]:
            if not visited[node]:
                queue.append(node)
                count += 1
                visited[node] = visited[x] + 1

    print(count)