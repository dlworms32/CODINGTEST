"""
    특정 거리의 도시 찾기
"""
import sys
from collections import deque

N, M, K, X = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N + 1)]
step = [0] * (N + 1)

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)

def bfs(x):
    queue = deque()
    queue.append(x)
    step[x] = 1

    while queue:
        cx = queue.popleft()

        for nx in graph[cx]:
            if step[nx] == 0:
                step[nx] = step[cx] + 1

                if step[nx] < (K + 1):
                    queue.append(nx)

bfs(X)
flag = False
for i in range(N + 1):
    if step[i] == (K + 1):
        print(i)
        flag = True

if not flag:
    print(-1)