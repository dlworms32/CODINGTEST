"""
    효율적인 해킹
    시간 빡빡 PyPy3로 제출
"""
import sys
from collections import deque

# N : 컴퓨터 개수, M : 신뢰 관계
N, M = map(int, sys.stdin.readline().split())

grape = [[] for _ in range(N + 1)]


for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    grape[B].append(A)

def bfs(index):
    queue = deque()
    visited = [0] * (N + 1)
    queue.append(index)
    visited[index] = True
    count = 1
    while queue:
        n = queue.popleft()  # 다음 인덱스

        for node in grape[n]:
            if not visited[node]:
                queue.append(node)
                visited[node] = True
                count += 1

    return count


results = [bfs(i) for i in range(1, N + 1)]
max_result = max(results)

for i in range(N):
    if results[i] == max_result:
        sys.stdout.write('{} '.format(i + 1))