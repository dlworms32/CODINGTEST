"""
    트리의 부모 찾기
"""
import sys
from collections import deque

N = int(sys.stdin.readline())

result = [0] * (N + 1)
visited = [False] * (N + 1)
tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())

    tree[a].append(b)
    tree[b].append(a)

queue = deque()
queue.append(1)
visited[1] = True

while queue:
    parent = queue.popleft()

    for child in tree[parent]:
        if not visited[child]:  # 방문하지 않은 경우
            result[child] = parent
            visited[child] = True
            queue.append(child)

for i in range(2, N + 1):
    print(result[i])